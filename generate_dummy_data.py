from api.models import IpoInfo  # Replace `myapp` with the name of your Django app
from random import randint, uniform
from datetime import datetime, timedelta
import random

# Helper function to generate random dates
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Generate 10 dummy IPO entries
for i in range(10):
    company_name = f"Company {chr(65+i)}"
    company_logo_path = f"https://example.com/logos/company_{chr(65+i).lower()}.png"
    price_band = f"{randint(50, 500)}-{randint(501, 1000)}"
    open_date = random_date(datetime(2023, 1, 1), datetime(2023, 12, 31)).strftime('%Y-%m-%d')
    close_date = (datetime.strptime(open_date, '%Y-%m-%d') + timedelta(days=3)).strftime('%Y-%m-%d')
    issue_size = f"{randint(10, 100)} Cr"
    issue_type = random.choice(["Fresh Issue", "Offer for Sale", "Both"])
    status = random.choice([0, 1])  # 0 for inactive, 1 for active
    ipo_price = f"{randint(100, 500)}"
    listing_price = f"{randint(501, 1000)}"
    listing_gain = f"{uniform(0.1, 2.0):.2f}x"
    listing_date = (datetime.strptime(close_date, '%Y-%m-%d') + timedelta(days=7)).strftime('%Y-%m-%d')
    cmp = f"{randint(500, 1500)}"
    current_return = f"{uniform(5, 20):.2f}%"
    rhp = f"https://example.com/rhp/company_{chr(65+i).lower()}.pdf"
    drhp = f"https://example.com/drhp/company_{chr(65+i).lower()}.pdf"

    # Create and save the entry
    ipo_info = IpoInfo(
        company_logo_path=company_logo_path,
        company_name=company_name,
        price_band=price_band,
        open_date=open_date,
        close_date=close_date,
        issue_size=issue_size,
        issue_type=issue_type,
        status=status,
        ipo_price=ipo_price,
        listing_price=listing_price,
        listing_gain=listing_gain,
        listing_date=listing_date,
        cmp=cmp,
        current_return=current_return,
        rhp=rhp,
        drhp=drhp
    )
    ipo_info.save()

print("Dummy data added successfully!")
