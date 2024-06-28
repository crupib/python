# iterate over a pd.DataFrame
import pandas as pd

df = pd.DataFrame(
    {'col1':range(5,15), 
     'col2':range(10,20), 
     'col3':list('abcdefghij')})

def iterate_dataframe(df):
    # Real hard work here
    result = df['col1'] * (df['col2']**2)
    return result
    
def main():
  from verstack import Multicore
  worker = Multicore()
  result = worker.execute(iterate_dataframe, df)
  print(result)
if __name__ == "__main__":
     main()
