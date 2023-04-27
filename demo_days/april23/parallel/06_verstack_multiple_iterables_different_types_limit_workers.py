# iterate over a pd.DataFrame and a list
import pandas as pd
iterable_list = list(range(0,10))

iterable_df = pd.DataFrame(
    {'col1':range(5,15), 
     'col2':range(10,20), 
     'col3':list('abcdefghij')})

def iterate_dataframe_and_iterable(iterable, df):
    # Real hard work here
    result = df['col1'] * iterable / (df['col2']**2)
    return result    
def main():
  from verstack import Multicore
  worker = Multicore(multiple_iterables = True,
                  workers = 2) # notice the workers parameter
  result = worker.execute(iterate_dataframe_and_iterable, [iterable_list, iterable_df])
  print(result)

if __name__ == "__main__":
     main()
