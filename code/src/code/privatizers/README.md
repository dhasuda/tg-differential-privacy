# Privatizers

In this folder, you'll find all the privatization method implemented as `privatizers`. Each one has its own particularities, including the type of data it processes.

Below, you can find a little description of each method. In the `data adapters` folder, there are implementations to transform the raw data into a format the privatizer can understand.

## Coin Privatizer
  This is one of the most simple methods of privatizing data. This algoritm accept as input only boolean values in the form of lists.

  So, let's say that there is a dataset with info about wheter people smoke and if they are obese. One example of data this class can understand is:
  ```
    [
      [True, True],
      [True, False],
      [False, True],
      [False, False]
    ]
  ```
  In this example, each list inside the bigger list is one person's data. The first element in one person's data is wheter they smoke or not, and the other bool corresponds to where this person is obese or not.