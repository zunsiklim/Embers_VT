from Util import common

con = common.getDBConnection()
cur = con.cursor()
sql = "select country from s_stock_country where stock_index=?"
cur.execute(sql,("MERVAL",))
result = cur.fetchone()
country = result[0]
print country