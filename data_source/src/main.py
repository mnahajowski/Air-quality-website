import schedule
import time
import get_stations
import get_pollution_data


schedule.every().day.at('00:00').do(get_stations.main)
schedule.every().hour.at(':05').do(get_pollution_data.main)


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(60)
