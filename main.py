from testing.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        # bot.change_currency()
        bot.select_palce('New York')
        bot.dates()
        bot.select_occupancy()
        print(bot.report_results())
except Exception as e:
    if 'in PATH' in str(e):
        print("You are trying to exceute prgram from command line")
    else:
        raise
