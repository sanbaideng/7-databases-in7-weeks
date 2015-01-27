def get_data():
    select_time = calculate_time()
    logger.info("select time:"+select_time)
    sql = "select file_name,message from logsdb.app_logs_record " \
          "where log_time >"+"'"+select_time+"'" \
          "and level="+"'ERROR'" \
          "order by log_time desc"
    conn = get_con()

    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results