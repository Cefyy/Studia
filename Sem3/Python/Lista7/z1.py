import asyncio
import aiohttp
import prywatne



async def fetch_yahoo_finance(session):
    try:
        url = "https://yahoo-finance166.p.rapidapi.com/api/stock/get-price"
        querystring = {"region":"US","symbol":"SPY"}
        headers = {
            "x-rapidapi-key": prywatne.RAPIDAPI_KEY,
            "x-rapidapi-host": prywatne.RAPIDAPI_HOST
        }
        async with session.get(url,headers=headers,params=querystring) as response:
            response.raise_for_status()
            data = await response.json()
            return data
    except aiohttp.ClientError as e:
        print(f"Yahoo Finance Error: {e}")
        return None
    except Exception as e:
        print(f"unexcpected error in yahoo finance: {e}")
        return None
    
    
async def fetch_streaming(session):
    try: 
        url = "https://streaming-availability.p.rapidapi.com/shows/search/title"
        querystring ={"title": "Stranger Things","country": "us","series_granularity":"episode","show_type":"series","output_language":"en"}
        headers = {
            "x-rapidapi-key": prywatne.RAPIDAPI_KEY,
            "x-rapidapi-host": prywatne.RAPIDAPI_HOST2
        }
        async with session.get(url,headers=headers,params=querystring) as response:
            response.raise_for_status()
            data = await response.json()
            return data
    except aiohttp.ClientError as e:
        print(f"Streaming Error: {e}")
        return None
    except Exception as e:
        print(f"unexcpected error in streaming: {e}")
        return None
async def main():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            fetch_yahoo_finance(session),
            fetch_streaming(session)
        )
        yahoo_data,streaming_data = results
        if yahoo_data:
            try:
                print(yahoo_data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']) #cena S&P 500 na otwarcie marketu
            except Exception as e:
                print(f"Error in yahoo finance parsing: {e}")
        else:
            print("Unable to get data") 
        print("=================================")
        if streaming_data:
            try:
                print(streaming_data[0]['title']) #tytuł
            except Exception as e:
                print(f"Error in streaming parsing: {e}") 
        else:
            print("Unable to get data") 
        

if __name__ == "__main__":
    asyncio.run(main())
