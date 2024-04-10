# Importing required libraries
import json
import csv

def list_to_csv(data, file_path):
    """
    Convert JSON data to CSV format and save it to a file.

    Args:
    data (str): JSON data string.
    file_path (str): Path to save the CSV file.
    """
    # Load JSON data
    json_data = json.loads(data)

    # Extracting course details
    courses = json_data['results']

    # Extracting column names
    column_names = ["Title", "URL", "Price", "Instructor", "Language"]

    # Writing data to CSV file
    with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)  # Writing column headers
        for course in courses:
            title = course['title']
            url = 'https://www.udemy.com' + course['url']
            price = course['price_detail']['price_string']
            instructor = ', '.join([instructor['display_name'] for instructor in course['visible_instructors']])
            language = course['locale']['title']
            writer.writerow([title, url, price, instructor, language])

# Sample usage
jsonData = '''
{
    "count": 76,
    "next": "https://www.udemy.com/api-2.0/users/me/subscribed-courses/?page=2",
    "previous": null,
    "results": [
        {
            "_class": "course",
            "id": 2371066,
            "title": "Learn to Code with Python 3",
            "url": "/course/python3-for-beginners/learn/",
            "is_paid": true,
            "price": "19,99 €",
            "price_detail": {
                "amount": 19.99,
                "currency": "EUR",
                "price_string": "19,99 €",
                "currency_symbol": "€"
            },
            "price_serve_tracking_id": "I90WhpccQ1qYcGNxXG6cRA",
            "visible_instructors": [
                {
                    "_class": "user",
                    "id": 12013100,
                    "title": "Joseph Delgadillo",
                    "name": "Joseph",
                    "display_name": "Joseph Delgadillo",
                    "job_title": "Best-Selling Instructor",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/12013100_e696_6.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/12013100_e696_6.jpg",
                    "initials": "JD",
                    "url": "/user/josephdelgadillo2/"
                }
            ],
            "image_125_H": "https://img-c.udemycdn.com/course/125_H/2371066_74f8_5.jpg",
            "image_240x135": "https://img-c.udemycdn.com/course/240x135/2371066_74f8_5.jpg",
            "is_practice_test_course": false,
            "image_480x270": "https://img-c.udemycdn.com/course/480x270/2371066_74f8_5.jpg",
            "published_title": "python3-for-beginners",
            "tracking_id": "sjj6Igi7TJiUmtmktHH42A",
            "locale": {
                "_class": "locale",
                "locale": "en_US",
                "title": "English (US)",
                "english_title": "English (US)",
                "simple_english_title": "English"
            }
        },
        {
            "_class": "course",
            "id": 614772,
            "title": "The Complete Cyber Security Course : Hackers Exposed!",
            "url": "/course/the-complete-internet-security-privacy-course-volume-1/learn/",
            "is_paid": true,
            "price": "19,99 €",
            "price_detail": {
                "amount": 19.99,
                "currency": "EUR",
                "price_string": "19,99 €",
                "currency_symbol": "€"
            },
            "price_serve_tracking_id": "wjPXtw9kRfSe8xZQa0zuFg",
            "visible_instructors": [
                {
                    "_class": "user",
                    "id": 15858120,
                    "title": "Nathan House",
                    "name": "Nathan",
                    "display_name": "Nathan House",
                    "job_title": "Leading Cyber Security Expert - CEO of StationX",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/15858120_4fac.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/15858120_4fac.jpg",
                    "initials": "NH",
                    "url": "/user/nathan-house/"
                }
            ],
            "image_125_H": "https://img-c.udemycdn.com/course/125_H/614772_233b_9.jpg",
            "image_240x135": "https://img-c.udemycdn.com/course/240x135/614772_233b_9.jpg",
            "is_practice_test_course": false,
            "image_480x270": "https://img-c.udemycdn.com/course/480x270/614772_233b_9.jpg",
            "published_title": "the-complete-internet-security-privacy-course-volume-1",
            "tracking_id": "jbgNvc8XQE2t00v61OELoA",
            "locale": {
                "_class": "locale",
                "locale": "en_US",
                "title": "English (US)",
                "english_title": "English (US)",
                "simple_english_title": "English"
            }
        },
        {
            "_class": "course",
            "id": 859184,
            "title": "Les Data Sciences de A à Z",
            "url": "/course/les-data-sciences-de-a-a-z/learn/",
            "is_paid": true,
            "price": "24,99 €",
            "price_detail": {
                "amount": 24.99,
                "currency": "EUR",
                "price_string": "24,99 €",
                "currency_symbol": "€"
            },
            "price_serve_tracking_id": "8wGOQI-4SjGTdIceqm2jgw",
            "visible_instructors": [
                {
                    "_class": "user",
                    "id": 22113450,
                    "title": "Hadelin de Ponteves",
                    "name": "Hadelin",
                    "display_name": "Hadelin de Ponteves",
                    "job_title": "Passionate AI Instructor",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/22113450_6fb5_3.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/22113450_6fb5_3.jpg",
                    "initials": "HD",
                    "url": "/user/hadelin-de-ponteves/"
                },
                {
                    "_class": "user",
                    "id": 27129696,
                    "title": "SuperDataScience Team",
                    "name": "SuperDataScience",
                    "display_name": "SuperDataScience Team",
                    "job_title": "Helping Data Scientists Succeed",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/27129696_acc1_4.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/27129696_acc1_4.jpg",
                    "initials": "ST",
                    "url": "/user/superdatascience-team/"
                }
            ],
            "image_125_H": "https://img-c.udemycdn.com/course/125_H/859184_d252_3.jpg",
            "image_240x135": "https://img-c.udemycdn.com/course/240x135/859184_d252_3.jpg",
            "is_practice_test_course": false,
            "image_480x270": "https://img-c.udemycdn.com/course/480x270/859184_d252_3.jpg",
            "published_title": "les-data-sciences-de-a-a-z",
            "tracking_id": "5GyfeVhNSdqlNvCuGFeR7g",
            "locale": {
                "_class": "locale",
                "locale": "fr_FR",
                "title": "Français (France)",
                "english_title": "French (France)",
                "simple_english_title": "French"
            }
        },
        {
            "_class": "course",
            "id": 2600016,
            "title": "Hacking Éthique : Sécurité des réseaux",
            "url": "/course/hacking-ethique-securite-reseau-wifi/learn/",
            "is_paid": true,
            "price": "24,99 €",
            "price_detail": {
                "amount": 24.99,
                "currency": "EUR",
                "price_string": "24,99 €",
                "currency_symbol": "€"
            },
            "price_serve_tracking_id": "3i1QEYYZRTq6Ignr5e76RQ",
            "visible_instructors": [
                {
                    "_class": "user",
                    "id": 27057692,
                    "title": "Michel Kartner",
                    "name": "Michel",
                    "display_name": "Michel Kartner",
                    "job_title": "Fondateur des sites Cyberini et Le Blog Du Hacker",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/27057692_dde9_2.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/27057692_dde9_2.jpg",
                    "initials": "MK",
                    "url": "/user/michel-kartner/"
                },
                {
                    "_class": "user",
                    "id": 125293768,
                    "title": "Cyberini Formations",
                    "name": "Cyberini",
                    "display_name": "Cyberini Formations",
                    "job_title": "La Sécurité Informatique Accessible à Tous",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/125293768_046a.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/125293768_046a.jpg",
                    "initials": "CF",
                    "url": "/user/cyberini/"
                },
                {
                    "_class": "user",
                    "id": 38032450,
                    "title": "Le Blog Du Hacker",
                    "name": "Le Blog Du",
                    "display_name": "Le Blog Du Hacker",
                    "job_title": "",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/38032450_ed9c.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/38032450_ed9c.jpg",
                    "initials": "LH",
                    "url": "/user/le-blog-du-hacker/"
                }
            ],
            "image_125_H": "https://img-c.udemycdn.com/course/125_H/2600016_47d9_2.jpg",
            "image_240x135": "https://img-c.udemycdn.com/course/240x135/2600016_47d9_2.jpg",
            "is_practice_test_course": false,
            "image_480x270": "https://img-c.udemycdn.com/course/480x270/2600016_47d9_2.jpg",
            "published_title": "hacking-ethique-securite-reseau-wifi",
            "tracking_id": "7F6rcSNaTn29qLKk5ToEUQ",
            "locale": {
                "_class": "locale",
                "locale": "fr_FR",
                "title": "Français (France)",
                "english_title": "French (France)",
                "simple_english_title": "French"
            }
        },
        {
            "_class": "course",
            "id": 2845456,
            "title": "SCRUM et le best-of des méthodes agiles de gestion de projet",
            "url": "/course/scrum-et-le-best-of-des-methodes-agiles-de-gestion-de-projet/learn/",
            "is_paid": true,
            "price": "24,99 €",
            "price_detail": {
                "amount": 24.99,
                "currency": "EUR",
                "price_string": "24,99 €",
                "currency_symbol": "€"
            },
            "price_serve_tracking_id": "EGqE6B5tT1m90pCZyzJdIw",
            "visible_instructors": [
                {
                    "_class": "user",
                    "id": 28253010,
                    "title": "Pascal Lochert",
                    "name": "Pascal",
                    "display_name": "Pascal Lochert",
                    "job_title": "Consultant-Formateur",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/28253010_4da4.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/28253010_4da4.jpg",
                    "initials": "PL",
                    "url": "/user/lochert-pascal/"
                },
                {
                    "_class": "user",
                    "id": 33198826,
                    "title": "Catherine Kong",
                    "name": "Catherine",
                    "display_name": "Catherine Kong",
                    "job_title": "Consultant IT, Test Manager",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/33198826_3ea5_2.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/33198826_3ea5_2.jpg",
                    "initials": "CK",
                    "url": "/user/kong-catherine/"
                }
            ],
            "image_125_H": "https://img-c.udemycdn.com/course/125_H/2845456_7e80_5.jpg",
            "image_240x135": "https://img-c.udemycdn.com/course/240x135/2845456_7e80_5.jpg",
            "is_practice_test_course": false,
            "image_480x270": "https://img-c.udemycdn.com/course/480x270/2845456_7e80_5.jpg",
            "published_title": "scrum-et-le-best-of-des-methodes-agiles-de-gestion-de-projet",
            "tracking_id": "IXSupiqQQ86F0jPgrHM0ew",
            "locale": {
                "_class": "locale",
                "locale": "fr_FR",
                "title": "Français (France)",
                "english_title": "French (France)",
                "simple_english_title": "French"
            }
        },
        {
            "_class": "course",
            "id": 3486282,
            "title": "5G RF Planning",
            "url": "/course/5g-rf-planning/learn/",
            "is_paid": true,
            "price": "19,99 €",
            "price_detail": {
                "amount": 19.99,
                "currency": "EUR",
                "price_string": "19,99 €",
                "currency_symbol": "€"
            },
            "price_serve_tracking_id": "SyBOCb1gTBKfvKQDR6u3lw",
            "visible_instructors": [
                {
                    "_class": "user",
                    "id": 126133636,
                    "title": "Honey Charnalia",
                    "name": "Honey",
                    "display_name": "Honey Charnalia",
                    "job_title": "Trainer and Telecom Industry expert",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/126133636_530b_2.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/126133636_530b_2.jpg",
                    "initials": "HC",
                    "url": ""
                }
            ],
            "image_125_H": "https://img-c.udemycdn.com/course/125_H/3486282_4182.jpg",
            "image_240x135": "https://img-c.udemycdn.com/course/240x135/3486282_4182.jpg",
            "is_practice_test_course": false,
            "image_480x270": "https://img-c.udemycdn.com/course/480x270/3486282_4182.jpg",
            "published_title": "5g-rf-planning",
            "tracking_id": "9hytw5QGTmS5k9e_EadROA",
            "locale": {
                "_class": "locale",
                "locale": "en_US",
                "title": "English (US)",
                "english_title": "English (US)",
                "simple_english_title": "English"
            }
        },
        {
            "_class": "course",
            "id": 2513790,
            "title": "Agile Scrum for Beginners + Scrum Master Certification",
            "url": "/course/scrum-training-scrum-master-certification-agile-project-management/learn/",
            "is_paid": true,
            "price": "19,99 €",
            "price_detail": {
                "amount": 19.99,
                "currency": "EUR",
                "price_string": "19,99 €",
                "currency_symbol": "€"
            },
            "price_serve_tracking_id": "qSk9iGXlT5y79NlnpDPSiA",
            "visible_instructors": [
                {
                    "_class": "user",
                    "id": 7519182,
                    "title": "Umer Waqar, PMP",
                    "name": "Umer",
                    "display_name": "Umer Waqar, PMP",
                    "job_title": "Project Management Instructor",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/7519182_1a56_2.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/7519182_1a56_2.jpg",
                    "initials": "UW",
                    "url": "/user/umerwaqar3/"
                }
            ],
            "image_125_H": "https://img-c.udemycdn.com/course/125_H/2513790_56bf.jpg",
            "image_240x135": "https://img-c.udemycdn.com/course/240x135/2513790_56bf.jpg",
            "is_practice_test_course": false,
            "image_480x270": "https://img-c.udemycdn.com/course/480x270/2513790_56bf.jpg",
            "published_title": "scrum-training-scrum-master-certification-agile-project-management",
            "tracking_id": "qmFiRDNQQq6OtmcBbOx3iw",
            "locale": {
                "_class": "locale",
                "locale": "en_US",
                "title": "English (US)",
                "english_title": "English (US)",
                "simple_english_title": "English"
            }
        },
        {
            "_class": "course",
            "id": 693188,
            "title": "Complete Guide to Elasticsearch",
            "url": "/course/elasticsearch-complete-guide/learn/",
            "is_paid": true,
            "price": "29,99 €",
            "price_detail": {
                "amount": 29.99,
                "currency": "EUR",
                "price_string": "29,99 €",
                "currency_symbol": "€"
            },
            "price_serve_tracking_id": "Ik9hLiVSTtCQnz44Wopk-g",
            "visible_instructors": [
                {
                    "_class": "user",
                    "id": 8092788,
                    "title": "Bo Andersen",
                    "name": "Bo",
                    "display_name": "Bo Andersen",
                    "job_title": "Lead Developer",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/8092788_2057_2.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/8092788_2057_2.jpg",
                    "initials": "BA",
                    "url": "/user/boandersen3/"
                }
            ],
            "image_125_H": "https://img-c.udemycdn.com/course/125_H/693188_6360_3.jpg",
            "image_240x135": "https://img-c.udemycdn.com/course/240x135/693188_6360_3.jpg",
            "is_practice_test_course": false,
            "image_480x270": "https://img-c.udemycdn.com/course/480x270/693188_6360_3.jpg",
            "published_title": "elasticsearch-complete-guide",
            "tracking_id": "_FdGMpuSQMW0081pVADvOg",
            "locale": {
                "_class": "locale",
                "locale": "en_US",
                "title": "English (US)",
                "english_title": "English (US)",
                "simple_english_title": "English"
            }
        },
        {
            "_class": "course",
            "id": 937678,
            "title": "Tableau A-Z: Hands-On Tableau Training for Data Science",
            "url": "/course/tableau10/learn/",
            "is_paid": true,
            "price": "24,99 €",
            "price_detail": {
                "amount": 24.99,
                "currency": "EUR",
                "price_string": "24,99 €",
                "currency_symbol": "€"
            },
            "price_serve_tracking_id": "DjLyzPOxTh6RuB6esCJfBQ",
            "visible_instructors": [
                {
                    "_class": "user",
                    "id": 2364054,
                    "title": "Kirill Eremenko",
                    "name": "Kirill",
                    "display_name": "Kirill Eremenko",
                    "job_title": "DS & AI Instructor",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/2364054_83cd_5.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/2364054_83cd_5.jpg",
                    "initials": "KE",
                    "url": "/user/kirilleremenko/"
                },
                {
                    "_class": "user",
                    "id": 27129696,
                    "title": "SuperDataScience Team",
                    "name": "SuperDataScience",
                    "display_name": "SuperDataScience Team",
                    "job_title": "Helping Data Scientists Succeed",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/27129696_acc1_4.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/27129696_acc1_4.jpg",
                    "initials": "ST",
                    "url": "/user/superdatascience-team/"
                },
                {
                    "_class": "user",
                    "id": 150405524,
                    "title": "Ligency Team",
                    "name": "Ligency",
                    "display_name": "Ligency Team",
                    "job_title": "Helping Data Scientists Succeed",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/150405524_94b0_9.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/150405524_94b0_9.jpg",
                    "initials": "LT",
                    "url": "/user/ligency-team/"
                }
            ],
            "image_125_H": "https://img-c.udemycdn.com/course/125_H/937678_abd2_3.jpg",
            "image_240x135": "https://img-c.udemycdn.com/course/240x135/937678_abd2_3.jpg",
            "is_practice_test_course": false,
            "image_480x270": "https://img-c.udemycdn.com/course/480x270/937678_abd2_3.jpg",
            "published_title": "tableau10",
            "tracking_id": "3DmUIhNARyujqgAG0fSLUg",
            "locale": {
                "_class": "locale",
                "locale": "en_US",
                "title": "English (US)",
                "english_title": "English (US)",
                "simple_english_title": "English"
            }
        },
        {
            "_class": "course",
            "id": 753174,
            "title": "Advanced SQL : The Ultimate Guide (2024)",
            "url": "/course/sql-advanced/learn/",
            "is_paid": true,
            "price": "19,99 €",
            "price_detail": {
                "amount": 19.99,
                "currency": "EUR",
                "price_string": "19,99 €",
                "currency_symbol": "€"
            },
            "price_serve_tracking_id": "pEik_qy7T7a_XTANb5kKdQ",
            "visible_instructors": [
                {
                    "_class": "user",
                    "id": 14078692,
                    "title": "Database Masters Training | 250,000+ Students Worldwide",
                    "name": "Database Masters Training",
                    "display_name": "Database Masters Training | 250,000+ Students Worldwide",
                    "job_title": "Oracle Architect & Best Selling Instructor",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/14078692_b9ed_18.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/14078692_b9ed_18.jpg",
                    "initials": "D|",
                    "url": "/user/mer-daaan/"
                },
                {
                    "_class": "user",
                    "id": 17308906,
                    "title": "Code Star Academy",
                    "name": "Code Star",
                    "display_name": "Code Star Academy",
                    "job_title": "Software Training Center | Over 250.000+ Successful Students",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/17308906_e099_10.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/17308906_e099_10.jpg",
                    "initials": "CA",
                    "url": "/user/omer-faruk-ince/"
                }
            ],
            "image_125_H": "https://img-c.udemycdn.com/course/125_H/753174_8624_14.jpg",
            "image_240x135": "https://img-c.udemycdn.com/course/240x135/753174_8624_14.jpg",
            "is_practice_test_course": false,
            "image_480x270": "https://img-c.udemycdn.com/course/480x270/753174_8624_14.jpg",
            "published_title": "sql-advanced",
            "tracking_id": "70PgK5jSQoOJa7sNwDxWEg",
            "locale": {
                "_class": "locale",
                "locale": "en_US",
                "title": "English (US)",
                "english_title": "English (US)",
                "simple_english_title": "English"
            }
        },
        {
            "_class": "course",
            "id": 757918,
            "title": "Talend Data Integration Course : Beginner to Expert",
            "url": "/course/talend-data-integration-course-beginner-to-expert/learn/",
            "is_paid": true,
            "price": "19,99 €",
            "price_detail": {
                "amount": 19.99,
                "currency": "EUR",
                "price_string": "19,99 €",
                "currency_symbol": "€"
            },
            "price_serve_tracking_id": "csjWLc8PReaTpPTOhD_XmQ",
            "visible_instructors": [
                {
                    "_class": "user",
                    "id": 20302686,
                    "title": "Kapil Chaitanya Kasarapu",
                    "name": "Kapil Chaitanya",
                    "display_name": "Kapil Chaitanya Kasarapu",
                    "job_title": "Lead Data Engineer",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/20302686_4b60.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/20302686_4b60.jpg",
                    "initials": "KK",
                    "url": "/user/kapil-kasarapu/"
                }
            ],
            "image_125_H": "https://img-c.udemycdn.com/course/125_H/757918_f064_2.jpg",
            "image_240x135": "https://img-c.udemycdn.com/course/240x135/757918_f064_2.jpg",
            "is_practice_test_course": false,
            "image_480x270": "https://img-c.udemycdn.com/course/480x270/757918_f064_2.jpg",
            "published_title": "talend-data-integration-course-beginner-to-expert",
            "tracking_id": "4jzFz4V6Tje1RPjKwRTXBg",
            "locale": {
                "_class": "locale",
                "locale": "en_US",
                "title": "English (US)",
                "english_title": "English (US)",
                "simple_english_title": "English"
            }
        },
        {
            "_class": "course",
            "id": 2391766,
            "title": "Qlik Sense[Français] : Formation Complète[A-Z]-BI [TP]-2022",
            "url": "/course/qlik-sencefrancais-formation-decouverte-par-la-pratique/learn/",
            "is_paid": true,
            "price": "22,99 €",
            "price_detail": {
                "amount": 22.99,
                "currency": "EUR",
                "price_string": "22,99 €",
                "currency_symbol": "€"
            },
            "price_serve_tracking_id": "vqVNsMosSP2nR-cg9hLQHg",
            "visible_instructors": [
                {
                    "_class": "user",
                    "id": 54702034,
                    "title": "BI/DATA/JAVA |FORMATION IT DATA[Intégration,Visualisation], Développement Web",
                    "name": "BI/DATA/JAVA",
                    "display_name": "BI/DATA/JAVA |FORMATION IT DATA[Intégration,Visualisation], Développement Web",
                    "job_title": "Consultant Indépendant en Informatique, Formateur IT",
                    "image_50x50": "https://img-c.udemycdn.com/user/50x50/54702034_f52b_4.jpg",
                    "image_100x100": "https://img-c.udemycdn.com/user/100x100/54702034_f52b_4.jpg",
                    "initials": "B|",
                    "url": "/user/maurice-g-3/"
                }
            ],
            "image_125_H": "https://img-c.udemycdn.com/course/125_H/2391766_a392_2.jpg",
            "image_240x135": "https://img-c.udemycdn.com/course/240x135/2391766_a392_2.jpg",
            "is_practice_test_course": false,
            "image_480x270": "https://img-c.udemycdn.com/course/480x270/2391766_a392_2.jpg",
            "published_title": "qlik-sencefrancais-formation-decouverte-par-la-pratique",
            "tracking_id": "D359A9RuSQ-ckp6RrXztXw",
            "locale": {
                "_class": "locale",
                "locale": "fr_FR",
                "title": "Français (France)",
                "english_title": "French (France)",
                "simple_english_title": "French"
            }
        }
    ]
}
'''

# Call the function
list_to_csv(jsonData, 'udemy_courses.csv')
