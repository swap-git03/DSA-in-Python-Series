
import csv
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

input_file = Path("orders_input.csv")
cleaned_file = Path("cleaned_orders.csv")
rejected_file = Path("rejected_orders.csv")

valid_count = 0
rejected_count = 0
skipped_count = 0
total_amount = 0

try:
    with (
        input_file.open("r", newline="", encoding="utf-8") as source,
        cleaned_file.open("w", newline="", encoding="utf-8") as clean_output,
        rejected_file.open("w", newline="", encoding="utf-8") as reject_output
    ):
        reader = csv.DictReader(source)

        clean_writer = csv.DictWriter(
            clean_output,
            fieldnames=["order_id", "amount"]
        )
        clean_writer.writeheader()

        rejected_writer = csv.DictWriter(
            reject_output,
            fieldnames=[
                "order_id", "customer", "amount",
                "status", "error_reason"
            ]
        )
        rejected_writer.writeheader()

        for row in reader:

            # Process only PAID orders
            if row["status"].strip().upper() != "PAID":
                skipped_count += 1
                continue

            # Validate each record independently
            try:
                raw_amount = row["amount"].strip()

                if not raw_amount:
                    raise ValueError("Missing amount")

                amount = int(raw_amount)

                if amount <= 0:
                    raise ValueError("Amount must be positive")

            except ValueError as error:
                rejected_count += 1

                rejected_writer.writerow({
                    **row,
                    "error_reason": str(error)
                })

                logging.warning(
                    "Rejected %s: %s",
                    row["order_id"],
                    error
                )

            else:
                clean_writer.writerow({
                    "order_id": row["order_id"],
                    "amount": amount
                })

                valid_count += 1
                total_amount += amount

    logging.info("Pipeline completed successfully.")

except FileNotFoundError:
    logging.error("Input file not found: %s", input_file)

except PermissionError:
    logging.error("Permission denied while accessing a file.")

except OSError:
    logging.exception("A file operation failed.")

finally:
    print("Pipeline execution ended.")

print("\n--- Pipeline Summary ---")
print("Valid orders:", valid_count)
print("Rejected orders:", rejected_count)
print("Skipped orders:", skipped_count)
print("Total valid amount:", total_amount)
