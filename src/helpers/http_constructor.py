import requests
import requests.exceptions

from src.helpers.logger import Logger


class HttpConstructor:

    def get(self, url, headers=None, params=None):
        try:
            r = requests.get(url, timeout=3, params=params, headers=headers)
            r.raise_for_status()
            return r
        except requests.exceptions.HTTPError as errh:
            if errh.response.status_code >= 500:
                Logger.log(errh, errh.response.url, logType='error')
                return errh.response
            Logger.log(errh, errh.response, logType='error')
            return errh.response

        except (requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                requests.exceptions.RequestException) as err:
                Logger.log(err, err, logType='error')

                return err.response

    def put(self, url, payload, headers=None, params=None):
        try:
            r = requests.put(url, timeout=3, data=payload,
                             params=params, headers=headers)
            r.raise_for_status()
            return r
        except requests.exceptions.HTTPError as errh:
            Logger.log(errh, errh.response, logType='error')
            return errh.response
        except (requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                requests.exceptions.RequestException) as err:
                Logger.log(err, err, logType='error')

                return err.response

    def post(self, url, json, headers=None, params=None):
        try:
            r = requests.post(url, timeout=3, json=json,
                              params=params, headers=headers)
            r.raise_for_status()
            return r
        except requests.exceptions.HTTPError as errh:
            Logger.log(errh, errh.response, logType='error')
            return errh.response
        except (requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                requests.exceptions.RequestException) as err:
                Logger.log(err, err, logType='error')

                return err.response
