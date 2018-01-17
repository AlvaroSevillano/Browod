from splinter import Browser
import time
import datetime
import pytz
import logging as logger
from profiles import get_profiles

list_days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo',
             'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
list_months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
               'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']


def instance_name():
    import sys
    from boto.ec2.connection import EC2Connection

    if len(sys.argv) != 2:
        print "Please provide instance ID"
        sys.exit(1)

    c = EC2Connection()
    r = c.get_all_instances([sys.argv[1], ])
    try:
        print r[0].instances[0].tags['Name']
    except:
        sys.exit(1)


def wait_until_text_present(browser, txt, waiting_time=120):

    cont = 0
    while cont <= waiting_time:
        if browser.is_text_present(txt):
            return 0
        else:
            cont += 1
            time.sleep(1)
    time.sleep(2.0)
    return 1


def wait_until_00():
    while True:
        actual_time = datetime.datetime.today()
        if actual_time.hour == 0:
            return
        else:
            time.sleep(3)


def wait_until_22():
    while True:
        actual_time = datetime.datetime.today()
        if actual_time.hour == 22:
            return
        else:
            time.sleep(3)


def wait_until_00_madrid():
    while True:
        actual_time = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
        if actual_time.hour == 00:
            return
        else:
            time.sleep(3)

def wait_until_2358_madrid():
    while True:
        actual_time = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
        if (actual_time.hour == 21 and actual_time.minute >= 58) or actual_time.hour >= 21:
            return
        else:
            time.sleep(3)

def wait_until_2158():
    while True:
        actual_time = datetime.datetime.today()
        if (actual_time.hour == 21 and actual_time.minute >= 58) or actual_time.hour >= 21:
            return
        else:
            time.sleep(3)


def get_string_check_date(today):
    str_template = 'Clases disponibles el {day} de {month} de {year}'
    list_strings = []
    for i in range(7):
        date = today + datetime.timedelta(days=i)
        list_strings.append(str_template.format(day=date.day,
                                                month=list_months[date.month-1],
                                                year=date.year))
    return list_strings


def reserva_clase(name):

    today = datetime.datetime.today()
    weekday = today.weekday()
    strings_check_date = get_string_check_date(today)
    int_time, list_prefix, input_line, wait_time = get_profiles(name)

    logger.info('Waiting until 2 minutes before')
    wait_until_2358_madrid()
    logger.info('Its time to start')

    logger.info('Trying Browser')
    browser = Browser()
    init_cont = 0
    while init_cont < 10:
        try:
            browser.visit('https://www.google.com')
            break
        except:
            time.sleep(1)
            init_cont += 1

    email, password = input_line.split('|')
    logger.info('Starting user {}'.format(email))
    password = password

    # Visit URL
    url = "https://aimharder.com/login"
    url_reservas = "https://komcrossfit.aimharder.com/schedule"
    url_out = "https://aimharder.com/Util/logout.php"

    logger.info('Visiting main web aimharder')
    browser.visit(url)

    if wait_until_text_present(browser, 'Keep me logged in', waiting_time=80):
        logger.error('Main web did not load')
        browser.visit(url_out)
        time.sleep(5)
        return
    if wait_until_text_present(browser, 'Forgot my password', waiting_time=80):
        logger.error('Main web did not load')
        browser.visit(url_out)
        time.sleep(5)
        return
    time.sleep(5)
    logger.info('Filling email and password')
    browser.fill('mail', email)
    browser.fill('pw', password)
    logger.info('Logging in')
    button = browser.find_by_id('loginSubmit')
    button.click()

    if wait_until_text_present(browser, 'Reservas', waiting_time=80):
        logger.error('Main web did not load')
        browser.visit(url_out)
        time.sleep(5)
        return
    browser.visit(url_reservas)

    for i in range(0, 6):
        logger.info('Waiting for {}'.format(strings_check_date[i]))
        if wait_until_text_present(browser, strings_check_date[i]):
            logger.error('Last day did not appear')
            browser.visit(url_out)
            time.sleep(5)
            return
        button = browser.find_by_id("nextDay")
        button.click()
        time.sleep(2)

    logger.info('Waiting for {}'.format(strings_check_date[6]))
    if wait_until_text_present(browser, strings_check_date[6]):
        logger.error('Last day did not appear')
        browser.visit(url_out)
        time.sleep(5)
        return

    logger.info('Waiting 15 seconds for everything correct')
    time.sleep(15)

    ok = False
    if list_days[weekday + 6] != 'Sabado':
        for prefix in list_prefix:
            button = browser.find_by_xpath("//div[span[contains(text(), \'{prefix}\')] and "
                                                 "span[contains(text(), \'{int_time}\')]]"
                                           "//a[contains(text(), 'Reservar')]".
                                           format(prefix=prefix, int_time=int_time))
            if len(button) > 0:
                button = button[0]
                ok = True
                break

        if not ok:
            logger.error('Configuracion no encontrada')
            browser.quit()
            return

        logger.info('Waiting until midnight')
        wait_until_00_madrid()

        logger.info('Waiting a few seconds')
        time.sleep(wait_time+10)

        logger.info('Pushing button to make reservation')
        button.click()
        if wait_until_text_present(browser, 'Cancelar reserva', waiting_time=20):
            print logger.error('Error in last step of reservation')
        else:
            logger.info('Reservation is ok')

    else:
        button1 = browser.find_by_xpath("//div[span[contains(text(), \'{prefix}\')] and "
                                                 "span[contains(text(), \'{int_time}\')]]"
                                           "//a[contains(text(), 'Reservar')]".
                                           format(prefix='Team', int_time='12:00 - 13:00'))

        logger.info('Waiting until midnight')
        wait_until_00_madrid()

        logger.info('Waiting a few seconds')
        time.sleep(wait_time + 10)

        logger.info('Pushing button to make reservation')
        button1.click()
        time.sleep(20)

        button2 = browser.find_by_xpath("//div[span[contains(text(), \'{prefix}\')] and "
                                        "span[contains(text(), \'{int_time}\')]]"
                                        "//a[contains(text(), 'Reservar')]".
                                        format(prefix='Open', int_time='11:00 - 12:00'))

        button2.click()
        time.sleep(20)

    browser.visit(url_out)
    time.sleep(10)

    browser.quit()
