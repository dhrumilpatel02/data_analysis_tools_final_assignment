Dataset Name:
Mental Health in Tech Survey

Dataset Description:
This dataset is from a 2014 survey that measures attitudes towards mental health and frequency of mental health disorders in the tech workplace.

Problem Statment:
How does the frequency of mental health illness and attitudes towards mental health vary by geographic location?

Data Source:
https://www.kaggle.com/osmi/mental-health-in-tech-survey

Variables the analysis is carried out on:
Country: Name of the countries the survey includes
state: If you live in the United States, which state or territory do you live in?
treatment: Have you sought treatment for a mental health condition?
seek_help: Does your employer provide resources to learn more about mental health issues and how to seek help?

Description of analysis:

-I uploaded "the mental_health_analysis.py" jupyter notebooks file for your reference, you can refer to the "analysis.py" file too for the same.

-We have to find the effects of mental health illness and attitudes towards mental health vary by geographic location.

-I decided to carry out the analysis of the United States of America.

-In the "analysis.py" file at first, I imported necessary libraries

-Then I imported the survey.csv dataset and made two different data frames to run the analysis on two different variables (seek_help and treatment)

-The reason to pick seek_help was that by this variable we can know if an employer provides resources to learn more about mental health issues and how to seek help. This shows a welcoming attitude from the employer's point of view which can be crucial in terms of initiation from the employees' end, as a human would be more comfortable to speak up or seek any kind of help if they are showed a soothing nature from their employer.
-The reason to pick treatment was that by this variable we can know if the employee has sought treatment for a mental health condition. This is a direct indication as to if an employee tries to seek help in terms of treatment for any kind of mental health condition.

-For better understanding of the variables and I renamed seek_help and treatment's categorical values to numerical values for smoother filtering.

-Now as I am taking only the data of the United States of America, I filtered null values from the column 'state' and selected the country like the USA so we are left with the USA as a country as the data in the state column consists only of states in the USA.

-Next, I selected values and counted them where employers provide resources to learn more about mental health issues and for employees who seek help, I did it by filtering out any value except "1" which depicts "Yes".

-So now as we have only positive values in the dataset, we can start visualizing the data. I decided a bar chart would be a good choice for visualization as it shall apt to depict the type of data that we have and it would be easy to correlate if we find any relationship between states.

-In the "seek_help.png" located in the new_branch files. We can see that states like California (CA), Washington (WA), New York (NY), Oregon (OR) have a big spike in terms of employees who seek treatment for a mental health condition.

-In the "treatment.png" located in the new_branch files. We can see that there is a positive correlation between states like California (CA), Washington (WA), New York (NY), Oregon (OR). But a significant negative correlation can be seen in the State of Texas (TX) if we compare it with the "seek_help.png".

-From this analysis, it can surely be said that states like California (CA), Washington (WA), New York (NY), Oregon (OR) have a positive correlation i.e. the employers welcoming attitude does convert into employees seeking treatment for mental illness.

-But there are also states like Texas (TX) where it is negatively correlated and the employers welcoming attitude does not directly convert into employees seeking treatment for mental illness.
