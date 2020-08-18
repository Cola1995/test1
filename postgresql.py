import psycopg2

conn = psycopg2.connect(database="skylar", user="postgres", password="", host="10.41.4.26", port="5360")
print("Opened database successfully")
index = 1
while(1):
    index += 1
    cur = conn.cursor()
    cur.execute("""INSERT INTO "public"."rptsvc_etalog_event"("id", "mid", "mission_id", "tpl_id", "gid", "risk_all", "risk_high", "risk_middle", "risk_low", "apt_count", "leak_count", "datascan_count", "baseline_count", "software_count", "score", "event_time", "event_date", "level", "name", "ip", "guid", "listen_port", "os_name") VALUES (%d, 'e27eebb96a970fedad1b25d24e888e68', NULL, 22, 1, 47, 3, 39, 5, 0, 0, 0, 47, 0, 53, '2020-08-13 16:11:30', '2020-08-13', 1, 'WIN-4BG09GJ4BQR', '192.168.88.179', 'B881ED0E-FB7F-40CF-ACD3-3E2F87B1B767', '80,135,445,49152,49153,49154,49155,49156,139,50237,50238,50239,50240,50241,50242,50243,', 'Windows 7 SP 1');"""%(36+index))
    conn.commit()
    print(index)
conn.close()