import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#TASK 1
# 1. Read the data
events_data = pd.read_csv("event_data_train.csv")

# 2. 
events_data['date'] = pd.to_datetime(events_data.timestamp, unit='s')

# 3. 
events_data['day']= events_data['date'].dt.day

# 4.
unique_users_per_day = events_data.groupby('day')['user_id'].nunique()
print(unique_users_per_day.head(10))

# 5.
unique_users_per_day.plot(kind='line', figsize=(10, 6), title='Unique Users per Day')
plt.xlabel('Day')
plt.ylabel('Number of Unique Users')
plt.show()

# 6.
pass_steps = events_data[events_data['action'] == 'passed'].groupby('user_id')['step_id'].nunique()

# 7.
pass_steps = pass_steps.reset_index(name='pass_steps')
print(pass_steps.head())

# 8.
users_events_data = pd.pivot_table(events_data, values='step_id', index='user_id', columns='action', aggfunc='count', fill_value=0)
users_events_data.reset_index(inplace=True)

# 9.
users_events_data.sum(axis=1).plot(kind='hist', bins=20, figsize=(10, 6), title='Distribution of Steps by Users')
plt.xlabel('Number of Steps')
plt.ylabel('Frequency')


#TASK 2 Submissions data preparation
# 1 Read the data
submissions_data = pd.read_csv("submissions_data_train.csv")

# 2.
submissions_data['date'] = pd.to_datetime(submissions_data['timestamp'], unit='s')

# 3.
submissions_data['day'] = submissions_data['date'].dt.date

# 4.
users_scores = pd.pivot_table(submissions_data, values='step_id', index='user_id', columns='submission_status', aggfunc='count', fill_value=0)
users_scores.reset_index(inplace=True)

# 5. Plot the histogram
users_scores.sum(axis=1).plot(kind='hist',)
plt.xlabel('Number of Submission Steps')
plt.ylabel('Frequency')
plt.show()



# Task 3:
# 1. From events_data leave only the unique values (by “user_id”, “day”) in columns “user_id”, “day”, and “timestamp”.
unique_events_data = events_data[['user_id', 'day', 'timestamp']].drop_duplicates()

# 2.
user_timestamps = unique_events_data.groupby('user_id')['timestamp'].apply(list)

# 3.
timestamp_diff = user_timestamps.apply(np.diff)

# 4.
gaped_data = pd.Series(np.concatenate(timestamp_diff.values))

# 5.
gaped_data_days = gaped_data / (24 * 60 * 60)

# 6.
quantile_90 = np.quantile(gaped_data_days, 0.9)
quantile_95 = np.quantile(gaped_data_days, 0.95)


# TASK 4
current_time_step = 1536772811
dropout_threshold = 2592000

# 1. Find the max timestamp for each user
last_timestamps = events_data.groupby('user_id')['timestamp'].max().reset_index()

# 2.
last_timestamps['is_gone_user'] = (current_time_step - last_timestamps['timestamp']) > dropout_threshold

# 3.
users_data = last_timestamps
print(users_data.head())


# TASK 5

# 1 Merge “users_scores” and “users_data” by user_id. Use outer merging.
users_data = pd.merge(users_scores, users_data, on='user_id', how='outer')

# 2
users_data.fillna(0, inplace=True)

# 3
users_data = pd.merge(users_data, users_events_data, on='user_id', how='outer')

# 4
unique_days = events_data.groupby('user_id')['day'].nunique().reset_index(name='unique_days')
users_data = pd.merge(users_data, unique_days, on='user_id', how='left')

# 5
initial_user_count = events_data['user_id'].nunique()
final_user_count = users_data['user_id'].nunique()
assert initial_user_count == final_user_count, "User counts do not match!"

# 6
users_data['passed_course'] = users_data['correct'] > 170

# 7
percent_passed = (users_data['passed_course'].sum() / len(users_data)) * 100

print(percent_passed)
