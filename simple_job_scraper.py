#!/usr/bin/env python3
"""
Simple Job Scraper - Interactive job scraping tool
Prompts user for job role and location, then displays results with fallback data.
"""
import sys
import os
import urllib.parse
from datetime import datetime


class JobListing:
    """Represents a job listing with all relevant information."""
    def __init__(self, job_title, company_name, location, job_description, salary, website_link, source_site):
        self.job_title = job_title
        self.company_name = company_name
        self.location = location
        self.job_description = job_description
        self.salary = salary
        self.website_link = website_link
        self.source_site = source_site


def get_user_input():
    """Get job role and location from user."""
    print("=== Job Scraper ===")
    print()
    
    # Get job role
    while True:
        role = input("Enter the job role you're looking for: ").strip()
        if role:
            break
        print("Please enter a valid job role.")
    
    # Get location
    location = input("Enter the location (or press Enter for 'Any'): ").strip()
    if not location:
        location = "Any"
    
    return role, location


def scrape_jobs(role, location):
    """Generate sample job listings since external APIs are not available."""
    print(f"\n🔍 Searching for '{role}' jobs in '{location}'...")
    print("Generating sample job listings from major companies...")
    print("Please wait...\n")
    
    # Note: To use real job APIs, set up your API keys in environment variables
    # For example: export JSEARCH_API_KEY="your_api_key_here"
    api_key = os.getenv('JSEARCH_API_KEY')
    
    if api_key and api_key != 'your_jsearch_api_key_here':
        print("API key detected - you can integrate with real job APIs here")
        # Here you would integrate with real APIs like JSearch, Indeed, etc.
    
    # For now, generate sample data
    return get_sample_jobs(role, location)


def get_sample_jobs(role, location):
    """Generate sample job listings when real APIs are not available."""
    # Sample jobs data - no API key needed for fallback
    
    # Create sample jobs from major tech companies
    sample_jobs_data = [
        {
            "title": f"{role} - Senior Level",
            "company": "Microsoft",
            "location": location if location != "Any" else "Seattle, WA",
            "description": f"We are seeking an experienced {role} to join our dynamic team. This role offers excellent growth opportunities, competitive compensation, and the chance to work on cutting-edge technology projects.",
            "salary": "$120,000 - $160,000",
            "source": "Fallback"
        },
        {
            "title": f"{role} - Mid Level",
            "company": "Google",
            "location": location if location != "Any" else "Mountain View, CA",
            "description": f"Join Google's innovative team as a {role}. Work on products used by billions of people worldwide. We offer competitive benefits, flexible work arrangements, and a collaborative environment.",
            "salary": "$110,000 - $150,000",
            "source": "Fallback"
        },
        {
            "title": f"Senior {role}",
            "company": "Apple",
            "location": location if location != "Any" else "Cupertino, CA",
            "description": f"Apple is seeking a Senior {role} to join our world-class engineering team. You'll work on innovative products that delight millions of customers worldwide.",
            "salary": "$150,000 - $200,000",
            "source": "Fallback"
        },
        {
            "title": f"{role} Specialist",
            "company": "Amazon",
            "location": location if location != "Any" else "Austin, TX",
            "description": f"Amazon is looking for a talented {role} to help us build the future of cloud computing and e-commerce. Join our team of innovators and make an impact on millions of customers.",
            "salary": "$105,000 - $145,000",
            "source": "Fallback"
        },
        {
            "title": f"Lead {role}",
            "company": "Meta",
            "location": location if location != "Any" else "Menlo Park, CA",
            "description": f"Meta is seeking a Lead {role} to help us connect the world through our family of apps and emerging technologies. Be part of building the next evolution of social technology.",
            "salary": "$140,000 - $180,000",
            "source": "Fallback"
        }
    ]
    
    jobs = []
    for job_data in sample_jobs_data:
        # Generate application link
        application_link = generate_application_link(
            job_data["company"], 
            role, 
            location
        )
        
        job = JobListing(
            job_title=job_data["title"],
            company_name=job_data["company"],
            location=job_data["location"],
            job_description=job_data["description"],
            salary=job_data["salary"],
            website_link=application_link,
            source_site=job_data["source"]
        )
        jobs.append(job)
    
    print(f"✓ Generated {len(jobs)} enhanced fallback jobs")
    return jobs


def generate_application_link(company_name, role, location):
    """Generate a realistic job application link."""
    # URL encode the search parameters
    role_encoded = urllib.parse.quote_plus(role)
    location_encoded = urllib.parse.quote_plus(location) if location != "Any" else ""
    company_encoded = urllib.parse.quote_plus(company_name)
    
    # Company-specific career page URLs
    company_lower = company_name.lower().replace(" ", "").replace(".", "")
    
    company_urls = {
        "microsoft": f"https://careers.microsoft.com/us/en/search-results?keywords={role_encoded}",
        "google": f"https://careers.google.com/jobs/results/?q={role_encoded}",
        "amazon": f"https://amazon.jobs/en/search?base_query={role_encoded}",
        "apple": f"https://jobs.apple.com/en-us/search?search={role_encoded}",
        "meta": f"https://www.metacareers.com/jobs/?q={role_encoded}",
        "netflix": f"https://jobs.netflix.com/search?q={role_encoded}",
        "tesla": f"https://www.tesla.com/careers/search/?query={role_encoded}",
        "spotify": f"https://www.lifeatspotify.com/jobs?q={role_encoded}",
        "uber": f"https://www.uber.com/careers/list/?query={role_encoded}",
        "airbnb": f"https://careers.airbnb.com/positions/?search={role_encoded}",
        "linkedin": f"https://careers.linkedin.com/jobs?keywords={role_encoded}",
        "salesforce": f"https://salesforce.wd1.myworkdayjobs.com/External_Career_Site?q={role_encoded}",
        "oracle": f"https://careers.oracle.com/jobs/#en/sites/jobsearch/requisitions?keyword={role_encoded}",
        "ibm": f"https://careers.ibm.com/search-jobs/?k={role_encoded}",
        "intel": f"https://jobs.intel.com/search-jobs?k={role_encoded}"
    }
    
    # Check if we have a specific URL for this company
    for company_key, url in company_urls.items():
        if company_key in company_lower:
            return url
    
    # Fallback to generic job search sites with the specific company and role
    fallback_urls = [
        f"https://www.indeed.com/jobs?q={role_encoded}+{company_encoded}&l={location_encoded}",
        f"https://www.linkedin.com/jobs/search/?keywords={role_encoded}%20{company_encoded}&location={location_encoded}",
        f"https://www.glassdoor.com/Jobs/jobs.htm?sc.keyword={role_encoded}%20{company_encoded}&locT=&locId="
    ]
    
    # Return the Indeed URL as it's most likely to have results
    return fallback_urls[0]


def display_results(jobs, role, location):
    """Display job search results."""
    print(f"\n" + "="*60)
    print(f"JOB SEARCH RESULTS")
    print(f"="*60)
    print(f"Search: {role}")
    print(f"Location: {location}")
    print(f"Total Jobs Found: {len(jobs)}")
    print(f"Search Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"="*60)
    
    if not jobs:
        print("No jobs found. Please try a different search term or location.")
        return
    
    for i, job in enumerate(jobs, 1):
        print(f"\n📋 JOB #{i}")
        print(f"├─ Company: {job.company_name}")
        print(f"├─ Role: {job.job_title}")
        print(f"├─ Location: {job.location}")
        print(f"├─ Salary: {job.salary or 'Not specified'}")
        print(f"├─ Description: {job.job_description[:100]}{'...' if len(job.job_description) > 100 else ''}")
        print(f"└─ Apply: {job.website_link or 'Not available'}")
        
        if i < len(jobs):
            print("─" * 60)


def save_results(jobs):
    """Ask user if they want to save results."""
    if not jobs:
        return
    
    save = input(f"\nWould you like to save these {len(jobs)} jobs to a file? (y/n): ").strip().lower()
    
    if save in ['y', 'yes']:
        # Create data directory if it doesn't exist
        os.makedirs('data', exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data/jobs_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Job Search Results\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total Jobs: {len(jobs)}\n")
                f.write("="*60 + "\n\n")
                
                for i, job in enumerate(jobs, 1):
                    f.write(f"JOB #{i}\n")
                    f.write(f"Company: {job.company_name}\n")
                    f.write(f"Role: {job.job_title}\n")
                    f.write(f"Location: {job.location}\n")
                    f.write(f"Salary: {job.salary or 'Not specified'}\n")
                    f.write(f"Description: {job.job_description}\n")
                    f.write(f"Website: {job.website_link or 'Not available'}\n")
                    f.write(f"Source: {job.source_site}\n")
                    f.write("-" * 60 + "\n")
            
            print(f"✓ Results saved to: {filename}")
        
        except Exception as e:
            print(f"✗ Error saving file: {e}")


def main():
    """Main application entry point."""
    try:
        # Get user input
        role, location = get_user_input()
        
        # Scrape jobs
        jobs = scrape_jobs(role, location)
        
        # Display results
        display_results(jobs, role, location)
        
        # Ask to save results
        save_results(jobs)
        
        print(f"\n🎉 Job search completed!")
        
    except KeyboardInterrupt:
        print(f"\n\n👋 Search cancelled by user.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try again or contact support.")


if __name__ == '__main__':
    main()
