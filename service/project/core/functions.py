# Standard API Envelope
def standardResponse(data=[], errors=[], **kwargs):
    return {"data":data, "errors":errors}