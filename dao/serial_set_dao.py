import util.link_mysql

class serial_set:
    db = util.link_mysql.link()

    def selectAll(self):
        sql = "SELECT * FROM serial_set"
        self.db.execute(sql)
        return self.db.get_execute()

    def update(self, data):
        sql = "UPDATE serial_set SET baud_rate="+data["baud_rate"]+",data_length="+data["data_length"]+",verification_mode=\""+data["verification_mode"]+"\",stop_bit="+data["stop_bit"]+",time_span="+data["time_span"]+",byte_stream_mode=\""+data["byte_stream_mode"]+"\",ip_addr=\""+data["ip_addr"]+"\",up_time="+data["up_time"]+";"
        self.db.execute(sql)


# print(serial_set().selectAll()[0])