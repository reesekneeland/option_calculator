import os
# Function to rename multiple files
def main():
    path="/home/reese/personal_projects/option_calculator/CSV_Files/"
    for filename in os.listdir(path):
        dataDate=filename[-14:];
        print(dataDate);
        my_dest = dataDate
        my_source =path + filename
        my_dest = path + my_dest
        # rename() function will
        # rename all the files
        os.rename(my_source, my_dest)
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()


   