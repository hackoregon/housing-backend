# Housing Project API Documentation

The housing api can currently be accessed at

<domain_name.com>/housing/

At this point only GET requests work, but eventually we'd like to be able to accept PUT requests from authorized users to add additional data.

Currently all requests return json as a default

##Endpoints

#### /affordable/
Lists all affordabilities in the database

"Affordable" objects come with 4 pieces of info:
- demographic - (Str) name of the demographic
- neighborhood - (Str) name of the neighborhood
- housing_size - (Str) the size of the house
- affordable - (Bool) True or False value if the 3 above variables are affordable or not. Measured at 30% of total income, not including utilities

##### Filters:
**housing_size**
- "Studio"
- "1-BR"
- "2-BR"
- "3-BR"
- "Homeowner"

**demographic**
- "Avg. Portland Household"
- "3-Person Extremely Low-Income"
- "Couple with Famly "
- "White"
- "Black "
- "Latino"
- "Native American"
- "Asian"
- "Senior"
- "Single Mother"
- "Foreign-Born"

#### Example Filter
Filters start with ? and are strung together with & symbols

```
http://127.0.0.1:8000/housing/affordable/?demographic=Avg. Portland Household&housing_size=3-BR
```

The above would return a json object containing all of the "Affordable" objects that matched the Average porlander

# Make sure your filters match EXACTLY!
Typos and all. This is left from the state that we received the data. So far we've only loaded it and have done no cleaning.



