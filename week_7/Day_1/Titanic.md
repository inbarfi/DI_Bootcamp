```python
import pandas as pd
import matplotlib.pyplot as plt
```


```python
titanic_df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
titanic_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df['Sex'].unique()
```




    array(['male', 'female'], dtype=object)




```python
male_data = titanic_df[titanic_df.Sex == 'male'].Survived.value_counts(normalize = True)
```


```python
female_data = titanic_df[titanic_df.Sex == 'female'].Survived.value_counts(normalize = True)
```


```python
female_data
```




    1    0.742038
    0    0.257962
    Name: Survived, dtype: float64




```python
male_data
```




    0    0.811092
    1    0.188908
    Name: Survived, dtype: float64




```python
fig, ax = plt.subplots(1,2,figsize=(13, 6))
ax[0].pie(male_data, labels = male_data.index.map({0:"Not survived", 1:"Survived"}), autopct='%1.1f%%')
ax[0].set_title('Male_passengers')
ax[1].pie(female_data, labels = female_data.index.map({0:"Not survived", 1:"Survived"}), autopct='%1.1f%%')
ax[1].set_title('Female_passengers')
plt.show()
```


    
![png](output_7_0.png)
    



```python
ax[0].set_title("male_passangers")
```




    Text(0.5, 1.0, 'male_passangers')




```python
plt.show()
```


```python
plt.figure(figsize = (10,5))
```




    <Figure size 720x360 with 0 Axes>




    <Figure size 720x360 with 0 Axes>



```python
plt.figure(figsize= (10,5))
titanic_df.Age.plot(kind="hist")
plt.xlabel('Age')
plt.title('Age distribution')
plt.show()

```


    
![png](output_11_0.png)
    



```python
plt.xlabel('Age')
```




    Text(0.5, 0, 'Age')




    
![png](output_12_1.png)
    



```python
titanic_df.groupby('Survived')["Age"].plot(kind='kde', figsize=(10, 5))
plt.legend()
plt.title('Age by density by survived')
plt.show()
```


    
![png](output_13_0.png)
    



```python

```
