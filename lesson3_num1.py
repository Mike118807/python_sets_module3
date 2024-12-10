# Python Sets Adventure
# Objective: The aim of this assignment is to deepen your understanding # and application of Python sets.
#
# Task 1: Flight Route Comparison Imagine you work for an airline and # need to compare the flight routes 
# of your airline with a competitor. You have two sets of flight destinations, one for each airline.
# Write a Python program to find out:
# 
# 1. Destinations that both airlines fly to.
# 
# 2. Destinations unique to your airline.
# 
# 3. Whether there are any destinations that neither airline shares.
#
# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Define sets of flight destinations.

our_routes = {"LAX", "JFK", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR" "BKK"}

#1. Destinations that both airlined fly to.

common_destinations = our_routes and competitor_routes
print("Destinations both airlines fly to:", common_destinations)

#2. Destinations unique to our ailine.

unique_to_our_airline = our_routes - competitor_routes
print("Destinations unique to our airlines:", unique_to_our_airline)

#3. Destination unique to competitors.

unique_to_competitor = competitor_routes - our_routes
print("Destination unique to competitor airlines:", unique_to_competitor)

#4. Check if there are any destinations that neither airline shares.

all_possible_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK"}
neither_airline_destinations = all_possible_destinations - (our_routes | competitor_routes)
print("Destinations neither airline shares:", neither_airline_destinations)