# MetabolicTracker
Metabolic Tracker for weight loss




---Purpose

-To have a dynamically adjusting metabolic rate for the user

-Use the dynamic value to predict weight loss progression over a specified course of time

---Total Daily Calories -> Expenditure Calories
- BMR is acheived using the revied Harris Benedict model
    **BMR = (10 × weight in kg) + (6.25 × height in cm) – (5 × age in years) + 5** --- Male
    **BMR = (10 × weight in kg) + (6.25 × height in cm) – (5 × age in years) – 161** -- Female

-- to create the predictive model we can take a running average of the 7 day calorie intake and calorie expidenture to see the total IO of calories and subtract that from total weight * 3500
---Height, Weight, Gender, age

--Future--
---- Compelete the running mean for weight and bmr.
-----

