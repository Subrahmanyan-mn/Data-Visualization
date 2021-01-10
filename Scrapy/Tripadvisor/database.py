import sqlite3

conn = sqlite3.connect('myhotels.db')

curr = conn.cursor()

#curr.execute(""" create table hotels (
 #                Hotel_Name text,
  #               Numberof_Rating text,
   #              Hotel_Type text )
    #                """)
                    
conn.commit()
conn.close()