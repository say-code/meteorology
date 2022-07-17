import util.link_mysql


class data:
    db = util.link_mysql.link()

    def selectAll(self):
        sql = "SELECT * FROM data"
        self.db.execute(sql)
        return self.db.get_execute()

    def insert(self, data):
        sql = "insert into data values ({},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(data[0], data[1], data[2],
                                                                                          data[3], data[4], data[5],
                                                                                          data[6], data[7], data[8],
                                                                                          data[9], data[10], data[11],
                                                                                          data[12], data[13])
        self.db.execute(sql)


