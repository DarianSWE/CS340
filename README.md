Grazioso Salvare Animal Rescue Dashboard
The Grazioso Salvare Dashboard is a web-based application designed to help identify dogs suited for search-and-rescue training by analyzing shelter data across the Austin, Texas region. 
Built in partnership with a non-profit operating five shelters, the dashboard filters dogs by age, breed, and gender criteria for specific rescue types: water rescue, mountain/wilderness, and disaster/individual tracking.

# Features
Interactive Filtering by rescue type (breed, age, gender)

Dynamic DataTable with sorting, filtering, and pagination

Visualizations using Pie Charts (breed distribution)

Geolocation Mapping with tooltips for selected animals

Real-Time Component Updates using Dash callbacks

# Rescue Type Criteria
Water Rescue: Labrador Retriever Mix, Chesapeake Bay Retriever, Newfoundland; Intact Female; 26–156 weeks

Mountain/Wilderness Rescue: German Shepherd, Malamute, Sheepdog, Husky, Rottweiler; Intact Male; 26–156 weeks

Disaster/Tracking: Doberman, German Shepherd, Golden Retriever, Bloodhound, Rottweiler; Intact Male; 20–300 weeks

# Technologies Used
MongoDB (document storage, geospatial queries)

Dash/Plotly (dashboard framework, visualizations)

Pandas (data transformation)

Dash Leaflet (interactive maps)

# Implementation Highlights
Integrated with existing MongoDB and AnimalShelter CRUD module

Built responsive layout with header, dropdown filter, data table, chart, and map

Implemented callback functions for interactivity and dynamic updates

Addressed data challenges like duplicate records and missing coordinates

# Running the App
Ensure MongoDB and CRUD module are set up.

Open the project in Jupyter Notebook.

Run all cells and follow the local URL to access the dashboard.

# Future Improvements
User authentication and role-based access

Enhanced filtering (dates, additional attributes)

Improved mapping services

Mobile responsiveness
