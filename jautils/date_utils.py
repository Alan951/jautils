from datetime import datetime

class DateUtils:
    
    @staticmethod
    def timestamp_to_date(timestamp):
        if(timestamp and timestamp != ''):
            return datetime.fromtimestamp(int(timestamp))
        
        return None

    @staticmethod
    def timestamp_to_str(timestamp):
        date = DateUtils.timestamp_to_date(timestamp)

        if(date):
            return date.strftime('%d-%m-%Y %H:%M:%S')

        return None

    @staticmethod
    def datetime_to_str(datetime):
        return datetime.strftime('%d-%m-%Y %H:%M:%S')