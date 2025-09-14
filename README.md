# Job Scraper

A simple Python-based job scraper that helps you search for jobs by role and location. This tool provides an interactive command-line interface for job searching with fallback sample data from major tech companies.

## Features

- 🔍 Interactive job search by role and location
- 💼 Sample job listings from major tech companies (Microsoft, Google, Apple, Amazon, Meta)
- 🔗 Direct application links to company career pages
- 💾 Option to save search results to text files
- 🛡️ Safe for GitHub - no hardcoded API keys

## Installation

1. Clone this repository:
```bash
git clone https://github.com/shahiilr/job_scraper.git
cd job_scraper
```

2. Run the script:
```bash
python3 simple_job_scraper.py
```

## Usage

1. Run the script:
```bash
python3 simple_job_scraper.py
```

2. Enter the job role you're looking for (e.g., "Software Engineer", "Data Scientist")

3. Enter the location (or press Enter for "Any")

4. View the search results with job details and application links

5. Choose whether to save the results to a file

## Example Output

```
=== Job Scraper ===

Enter the job role you're looking for: Software Engineer
Enter the location (or press Enter for 'Any'): San Francisco

🔍 Searching for 'Software Engineer' jobs in 'San Francisco'...
Generating sample job listings from major companies...
Please wait...

✓ Generated 5 enhanced sample jobs

============================================================
JOB SEARCH RESULTS
============================================================
Search: Software Engineer
Location: San Francisco
Total Jobs Found: 5
Search Date: 2024-09-15 01:30:00
============================================================

📋 JOB #1
├─ Company: Microsoft
├─ Role: Software Engineer - Senior Level
├─ Location: San Francisco
├─ Salary: $120,000 - $160,000
├─ Description: We are seeking an experienced Software Engineer to join our dynamic team...
└─ Apply: https://careers.microsoft.com/us/en/search-results?keywords=Software+Engineer
```

## API Integration

This tool is designed to be extended with real job APIs. To integrate with external APIs:

1. Set your API key as an environment variable:
```bash
export JSEARCH_API_KEY="your_api_key_here"
```

2. The script will detect the API key and can be extended to use real job search APIs

## File Structure

```
job_scraper/
├── simple_job_scraper.py    # Main application file
├── README.md                # This file
└── data/                    # Created when saving results
    └── jobs_YYYYMMDD_HHMMSS.txt
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Future Enhancements

- Integration with real job APIs (Indeed, LinkedIn, Glassdoor)
- Web interface using Flask or FastAPI
- Database storage for job listings
- Email notifications for new job matches
- Advanced filtering options

## Contact

For questions or suggestions, please open an issue on GitHub.
