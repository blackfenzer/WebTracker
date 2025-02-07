# your_app/tasks.py
from .scraper import LazadaScraper

from notifications.signals import notify


# @shared_task
# def scrape_lazada():
#     scraper = LazadaScraper()
#     items = TrackedItem.objects.all()
#     watching = [item.url for item in items]
#     scraper.scrape_urls(watching)
#     recent_two = ItemResult.objects.all().order_by("-created_at")[:2]
#     if len(recent_two) == 2:
#         current = recent_two[0]
#         prev = recent_two[1]
#         if current.current_price < prev.current_price:
#             # Notify users about the price drop
#             for item in items.filter(url=current.url):
#                 notify.send(
#                     sender=item,
#                     recipient=item.user,
#                     verb="Price drop alert",
#                     description=f"{item.name} is now {current.current_price}",
#                 )
#         else:
#             for item in items.filter(url=current.url):
#                 notify.send(
#                     sender=item,
#                     recipient=item.user,
#                     verb="Price remains the same",
#                     description=f"{item.name} is still {current.current_price}",
#                 )
#     scraper.close()
# from celery import shared_task
# from .models import TrackedItem, ItemResult, Notification


# @shared_task
# def scrape_lazada():
#     scraper = LazadaScraper()
#     items = TrackedItem.objects.all()
#     for item in items:
#         current_price = scraper.scrape_url(item.url)
#         last_result = (
#             ItemResult.objects.filter(url=item.url).order_by("-created_at").first()
#         )
#         if last_result and current_price < last_result.current_price:
#             Notification.objects.create(
#                 user=item.user,
#                 message=f"Price drop alert for {item.url}: {current_price}",
#             )
#         ItemResult.objects.create(url=item.url, current_price=current_price)
#     scraper.close()

from celery import shared_task
from .models import TrackedItem, ItemResult
from datetime import datetime
from celery import shared_task
from .models import TrackedItem, ItemResult
from datetime import datetime
from collections import defaultdict

@shared_task
def generate_price_drop_report():
    scraper = LazadaScraper()
    items = TrackedItem.objects.all()
    watching = [item.url for item in items]

    # Run the scraper to update prices
    scraper.find_many(watching)
    scraper.close()

    # Dictionary to store latest two records for each URL
    latest_results = defaultdict(list)

    # Group results by URL and store the last two records for each
    for result in ItemResult.objects.all().order_by("-created_at"):
        if len(latest_results[result.url]) < 2:
            latest_results[result.url].append(result)

    report_lines = []

    # Compare price changes for each tracked URL
    for url, results in latest_results.items():
        if len(results) == 2:
            current, prev = results  # The latest two entries
            if current.current_price < prev.current_price:
                report_lines.append(f'Price drop alert for {url}: {current.current_price}\n')
            else:
                report_lines.append(f'Price remains the same for {url}\n')

    # Write to the report file if there are updates
    if report_lines:
        with open('price_drop_report.txt', 'a') as report_file:
            report_file.write(f'Report generated on {datetime.now()}:\n')
            report_file.writelines(report_lines)
            report_file.write('\n')

if __name__ == "__main__":
    # Simulate the task execution
    generate_price_drop_report.apply_async()

    # Check the output file for the report
    with open('price_drop_report.txt', 'r') as report_file:
        report_content = report_file.read()
        print("Report Content:")
        print(report_content)

