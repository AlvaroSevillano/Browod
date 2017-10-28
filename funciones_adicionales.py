from splinter import Browser
import time
import datetime
import pytz
import logging as logger
from profiles import get_profiles

list_days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo',
             'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']


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


def reserva_clase(name):

    weekday = datetime.datetime.today().weekday()
    int_time, list_prefix, input_line, wait_time = get_profiles(name)

    logger.info('Waiting until 2 minutes before')
    wait_until_2358_madrid()
    logger.info('Its time to start')

    init_cont = 0
    while init_cont < 10:
        try:
            browser = Browser()
            init_cont = 10
        except:
            init_cont += 1

    email, password = input_line.split('|')
    logger.info('Starting user {}'.format(email))
    password = password

    # Visit URL
    url = "https://browod.com/booking"
    url_out = "https://browod.com/auth/logout"

    cont = 0
    while cont < 3:
        logger.info('Visiting main web browod')
        browser.visit(url)

        if wait_until_text_present(browser, 'ENTRAR', waiting_time=80):
            logger.error('Main web did not load')
            browser.visit(url_out)
            time.sleep(5)
            return
        if wait_until_text_present(browser, 'Olvidaste', waiting_time=80):
            logger.error('Main web did not load')
            browser.visit(url_out)
            time.sleep(5)
            return
        time.sleep(5)
        logger.info('Filling email and password')
        browser.fill('email', email)
        browser.fill('password', password)
        logger.info('Logging in')
        button = browser.find_by_text('ENTRAR')
        button.click()

        for i in range(0, 6):
            logger.info('Waiting for {}'.format(str(list_days[weekday + i])))
            if wait_until_text_present(browser, list_days[weekday + i]):
                logger.error('Last day did not appear')
                browser.visit(url_out)
                time.sleep(5)
                return
            button = browser.find_by_css(".next-day")
            button.click()

        logger.info('Waiting for {}'.format(str(list_days[weekday + 6])))
        if wait_until_text_present(browser, list_days[weekday + 6]):
            logger.error('Last day did not appear')
            browser.visit(url_out)
            time.sleep(5)
            return

        logger.info('Waiting 25 seconds for everything correct')
        time.sleep(25)

        ok = False
        for prefix in list_prefix:

            button = browser.find_by_xpath('//tr[td[contains(text(), \'{prefix}\')] and '
                                                'td[contains(text(), \'{int_time}\')]]//td[5]'.
                                                format(prefix=prefix, int_time=int_time))
            if len(button)>0:
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

        cont = 0

        logger.info('Pushing button to make reservation')
        button.click()
        if wait_until_text_present(browser, 'RESERVADA', waiting_time=20):
            if wait_until_text_present(browser, 'ESPERANDO', waiting_time=3):
                cont += 1
                print logger.error('Error in last step of reservation')
            else:
                print logger.info('Reservation is in LISTA DE ESPERA')
                return
        else:
            logger.info('Reservation is ok')
            return
        browser.visit(url_out)
        time.sleep(10)

    browser.quit()
