import psutil
import mysql.connector
from datetime import datetime

def get_process_info():
    try:
        conn = mysql.connector.connect(user='root', password='Zion@2022', host='localhost', database='mysql')
        cursor_conn = conn.cursor()

        for proc in psutil.process_iter(attrs=['pid', 'name', 'memory_info', 'num_threads', 'ppid', 'status', 'create_time']):
            info = proc.info
            pid = info['pid']
            name = info['name']
            memory_info = info.get('memory_info')  # Get the memory_info dictionary safely

            if memory_info:
                rss = memory_info.rss
                vms = memory_info.vms
            else:
                rss = vms = None

            num_threads = info['num_threads']
            ppid = info['ppid']
            status = info['status']
            create_time = datetime.fromtimestamp(info['create_time']).strftime('%Y-%m-%d %H:%M:%S')  # Convert to readable date format

            # Define SQL query with placeholders
            insert_query = """
                           INSERT INTO process_monitor(pid, name, rss, vms, num_threads, ppid, status, create_time)
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

            cursor_conn.execute(insert_query, (pid, name, rss, vms, num_threads, ppid, status, create_time))

        # Commit changes to the database
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close connections
        cursor_conn.close()
        conn.close()

get_process_info()