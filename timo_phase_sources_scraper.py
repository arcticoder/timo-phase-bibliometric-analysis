#!/usr/bin/env python3
"""
Ti-Mo Phase Sources Scraper

Searches Scopus and Google Scholar for publications related to Ti-Mo phase diagrams,
limited to 1930-2000, and tallies source frequencies.
"""

import os
import csv
import time
import requests
from collections import Counter
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TimoPhaseSourcesScraper:
    def __init__(self):
        self.scopus_api_key = os.getenv('SCOPUS_API_KEY')
        self.wos_api_key = os.getenv('WOS_API_KEY')
        self.source_counter = Counter()
          # Targeted search queries for Ti-Mo phase research (focused on specific terms)
        self.queries = [
            "Ti-Mo phase diagram",
            "Ti–Mo phase diagram", # em dash variant
            "titanium molybdenum phase diagram",
            "Ti-Mo solidus",
            "Ti–Mo solidus", # em dash variant
            "titanium molybdenum solidus",
            "Ti-Mo β-transus",
            "Ti–Mo β-transus", # em dash variant  
            "Ti-Mo beta transus",
            "Ti–Mo beta transus", # em dash variant
            "titanium molybdenum beta transus"
        ]
        
        # Date range: 1930-2000
        self.start_year = 1930
        self.end_year = 2000
        
        print(f"Initialized scraper for {len(self.queries)} queries covering {self.start_year}-{self.end_year}")

    def search_scopus(self, query):
        """Search Scopus API for a given query"""
        if not self.scopus_api_key:
            print("No Scopus API key found - skipping Scopus search")
            return []
            
        print(f"Searching Scopus for: '{query}'")
        
        # Scopus search URL
        url = "https://api.elsevier.com/content/search/scopus"
        
        # Build search query with date restrictions - simpler approach
        search_query = f'TITLE-ABS-KEY({query}) AND PUBYEAR > {self.start_year-1} AND PUBYEAR < {self.end_year+1}'
        
        headers = {
            'X-ELS-APIKey': self.scopus_api_key,
            'Accept': 'application/json'
        }
        
        params = {
            'query': search_query,
            'count': 25,  # Reduced for testing
            'start': 0,
            'field': 'dc:title,prism:publicationName,prism:coverDate,dc:creator'
        }
        
        results = []
        try:
            print(f"Query URL: {url}")
            print(f"Search query: {search_query}")
            
            response = requests.get(url, headers=headers, params=params)
            print(f"Response status: {response.status_code}")
            
            if response.status_code == 400:
                print(f"Bad request - Response: {response.text}")
                return []
                
            response.raise_for_status()
            
            data = response.json()
            
            if 'search-results' in data and 'entry' in data['search-results']:
                entries = data['search-results']['entry']
                
                for entry in entries:
                    # Extract publication source
                    source = entry.get('prism:publicationName', 'Unknown Source')
                    if source and source != 'Unknown Source':                        results.append({
                            'source': source,
                            'title': entry.get('dc:title', ''),
                            'date': entry.get('prism:coverDate', ''),
                            'database': 'Scopus',
                            'query': query
                        })
                        
                print(f"Found {len(results)} results from Scopus")
                
        except requests.exceptions.RequestException as e:
            print(f"Error searching Scopus: {e}")
        except Exception as e:
            print(f"Unexpected error with Scopus: {e}")
            
        return results

    def search_google_scholar(self, query):
        """Search Google Scholar using scholarly library with improved error handling"""
        print(f"Searching Google Scholar for: '{query}'")
        
        try:
            from scholarly import scholarly
            
            # Construct search query with year range
            full_query = f'{query} after:{self.start_year} before:{self.end_year}'
            print(f"Google Scholar query: {full_query}")
            
            results = []
            search_query = scholarly.search_pubs(full_query)
            
            # Limit to first 50 results but be more selective
            count = 0
            processed = 0
            for pub in search_query:
                processed += 1
                if count >= 50 or processed >= 100:  # Safety limit
                    break
                    
                try:
                    # Extract venue/source information
                    venue = pub.get('venue', '').strip()
                    title = pub.get('title', '').strip()
                    year = pub.get('year', '')
                    
                    # Skip if no venue information
                    if not venue:
                        continue
                    
                    # Check year range more carefully
                    year_valid = False
                    if year:
                        try:
                            year_int = int(str(year).strip())
                            if self.start_year <= year_int <= self.end_year:
                                year_valid = True
                            else:
                                continue  # Skip if outside year range
                        except (ValueError, TypeError):
                            # If year parsing fails, include it anyway
                            year_valid = True
                    else:
                        year_valid = True  # Include if no year info
                    
                    if venue and year_valid:
                        results.append({
                            'source': venue,
                            'title': title,
                            'year': year,
                            'database': 'Google Scholar',
                            'query': query
                        })
                        count += 1
                        print(f"  Found: {venue} ({year})")
                        
                    # Small delay to be respectful to Google Scholar
                    time.sleep(1.5)
                    
                except Exception as e:
                    print(f"Error processing Google Scholar result: {e}")
                    continue
                    
            print(f"Found {len(results)} valid results from Google Scholar for this query")
            
        except ImportError:
            print("scholarly library not installed - skipping Google Scholar search")
            print("Install with: pip install scholarly")
            return []
        except Exception as e:
            print(f"Error searching Google Scholar: {e}")
            return []
            
        return results

    def run_searches(self):
        """Execute all searches and collect results"""
        all_results = []
        
        for query in self.queries:
            print(f"\n--- Processing query: '{query}' ---")
            
            # Search Scopus
            scopus_results = self.search_scopus(query)
            all_results.extend(scopus_results)
            
            # Add delay between API calls
            time.sleep(2)
            
            # Search Google Scholar
            scholar_results = self.search_google_scholar(query)
            all_results.extend(scholar_results)
            
            # Add delay between queries
            time.sleep(3)
            
        return all_results

    def tally_sources(self, results):
        """Count frequency of each source"""
        for result in results:
            source = result['source'].strip()
            if source:
                self.source_counter[source] += 1
                
        print(f"\nTotal unique sources found: {len(self.source_counter)}")
        return self.source_counter

    def export_results(self, results, filename='source_counts.csv'):
        """Export source counts and detailed results to CSV"""
        # Export source frequency counts
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['source_title', 'count'])
            
            for source, count in self.source_counter.most_common():
                writer.writerow([source, count])
                
        print(f"Source counts exported to {filename}")
        
        # Export detailed results
        detailed_filename = filename.replace('.csv', '_detailed.csv')
        with open(detailed_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['source_title', 'article_title', 'year', 'database', 'query'])
            
            for result in results:
                writer.writerow([
                    result.get('source', ''),
                    result.get('title', ''),
                    result.get('year', result.get('date', '')),
                    result.get('database', ''),
                    result.get('query', '')
                ])
                
        print(f"Detailed results exported to {detailed_filename}")

    def print_summary(self):
        """Print summary of results"""
        print(f"\n{'='*60}")
        print("Ti-Mo Phase Sources Summary")
        print(f"{'='*60}")
        print(f"Search period: {self.start_year}-{self.end_year}")
        print(f"Total unique sources: {len(self.source_counter)}")
        print(f"Total publications: {sum(self.source_counter.values())}")
        
        print(f"\nTop 10 most cited sources:")
        print("-" * 40)
        for source, count in self.source_counter.most_common(10):
            print(f"{count:3d} – {source}")

def main():
    """Main execution function"""
    print("Ti-Mo Phase Sources Scraper")
    print("=" * 40)
    
    scraper = TimoPhaseSourcesScraper()
    
    # Run searches
    results = scraper.run_searches()
    
    if results:
        # Tally sources
        scraper.tally_sources(results)
        
        # Export to CSV (both summary and detailed)
        scraper.export_results(results)
        
        # Print summary
        scraper.print_summary()
    else:
        print("No results found. Check your API keys and internet connection.")

if __name__ == "__main__":
    main()
