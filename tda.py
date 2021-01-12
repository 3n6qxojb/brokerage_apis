# Use this script to make get an option chain using your TDameritrade account
# Documentation:
#   https://pypi.org/project/td-ameritrade-python-api/
#   https://developer.tdameritrade.com/

from td.client import TDClient
import os
import pprint


# This dictionary can be populated or the user will be prompted for values
TD = {
      # Get a TDamertirade client ID from https://developer.tdameritrade.com/
      'client_id' : '',
      'symbol' : 'MSFT', 
      'fromDate' : '2021-01-15:27',
      'toDate' : '2021-01-15:27',
      }
      

# Prompt the user for values (if needed)
if TD['client_id'] == '':
    TD['client_id'] = input('\n\nPlease input client ID\n\n')
if TD['symbol'] == '':
    TD['symbol'] = input('\n\nPlease input the symbol\n\n')


# Create a new session, a local credentials file is required.
TDSession = TDClient(
    client_id=TD['client_id'],
    redirect_uri='http://localhost',
    credentials_path=os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'state.json'
            )
    )


# Login to TDAmertrade to authenticate this app
TDSession.login()


# Get the options chain
option_chain = TDSession.get_options_chain(option_chain = { 
    # Documentation
    #   https://developer.tdameritrade.com/option-chains/apis/get/marketdata/chains
    'symbol' : TD['symbol'],
    'contractType' : 'CALL',
    'strikeCount' : 5,
    'range' : 'OTM',
    'fromDate' : TD['fromDate'],
    'toDate' : TD['toDate'],
    })


# Print returned json to the screen
print('\n')
pprint.pprint(option_chain)
input('\n\nPress Enter to close\n\n')

