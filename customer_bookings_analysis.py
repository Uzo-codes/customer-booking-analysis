# -*- coding: utf-8 -*-
"""
Customer Bookings Data Analysis
Author: Uzochi Chinedu
Description: A comprehensive data cleaning and exploratory analysis of a customer bookings dataset.
"""

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load the dataset
df = pd.read_csv("customer_bookings.csv")

# Preview dataset dimensions
print("Original Dataset Shape:", df.shape)

# Check for missing values and duplicates
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Entries:", df.duplicated().sum())

# Clean the dataset
df_cleaned = (
    df.drop_duplicates()
      .dropna()
      .drop(columns=["purchase_lead", "booking_origin"])
)

# Check cleaned dataset shape
print("\nCleaned Dataset Shape:", df_cleaned.shape)

# Save cleaned dataset
df_cleaned.to_csv("cleaned_customer_bookings.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_customer_bookings.csv'")

# View data types
print("\nData Types:\n", df_cleaned.dtypes)

# Frequency of trip types
trip_counts = df_cleaned["trip_type"].value_counts()
print("\nTrip Type Counts:\n", trip_counts)

# Bar plot: Trip type frequency
sns.countplot(x="trip_type", data=df_cleaned, palette="viridis")
plt.title("Distribution of Trip Types")
plt.xlabel("Trip Type")
plt.ylabel("Number of Bookings")
plt.tight_layout()
plt.show()

# Frequency of sales channels
sales_counts = df_cleaned["sales_channel"].value_counts()
print("\nSales Channel Counts:\n", sales_counts)

# Pie chart: Sales channel usage
sales_counts.plot.pie(autopct="%1.1f%%", startangle=90, colors=["#66c2a5", "#fc8d62"])
plt.title("Sales Channel Distribution")
plt.ylabel("")
plt.show()

# Flights by day
day_counts = df_cleaned["flight_day"].value_counts()
print("\nFlight Day Counts:\n", day_counts)

# Bar plot: Flights per day
sns.countplot(x="flight_day", data=df_cleaned, order=day_counts.index, palette="muted")
plt.title("Flights Per Day")
plt.xlabel("Day of the Week")
plt.ylabel("Number of Flights")
plt.tight_layout()
plt.show()

# Preferred seat & meal request totals
preferred = df_cleaned["wants_preferred_seat"].sum()
meals = df_cleaned["wants_in_flight_meals"].sum()
print(f"\nCustomers Who Wanted Preferred Seats: {preferred}")
print(f"Customers Who Wanted In-Flight Meals: {meals}")

# Horizontal bar chart: Services requested
sns.barplot(
    x=[preferred, meals],
    y=["Preferred Seats", "In-Flight Meals"],
    palette="coolwarm"
)
plt.title("Customer Service Requests")
plt.xlabel("Number of Requests")
plt.tight_layout()
plt.show()

# Average flight duration by trip type
duration_by_trip = df_cleaned.groupby("trip_type")["flight_duration"].mean()
print("\nAverage Flight Duration by Trip Type:\n", duration_by_trip)

# Bar chart: Average flight duration by trip type
duration_by_trip.plot(kind="bar", color="#8da0cb")
plt.title("Average Flight Duration by Trip Type")
plt.ylabel("Flight Duration (minutes)")
plt.xlabel("Trip Type")
plt.tight_layout()
plt.show()

# Average flight duration by day
duration_by_day = df_cleaned.groupby("flight_day")["flight_duration"].mean()
print("\nAverage Flight Duration by Day:\n", duration_by_day)

# Line plot: Flight duration across the week
sns.lineplot(x=duration_by_day.index, y=duration_by_day.values, marker="o", color="green")
plt.title("Average Flight Duration by Day")
plt.ylabel("Flight Duration (minutes)")
plt.xlabel("Day of the Week")
plt.tight_layout()
plt.show()
