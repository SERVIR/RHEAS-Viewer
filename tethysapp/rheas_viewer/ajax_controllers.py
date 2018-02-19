from django.http import JsonResponse, HttpResponse, Http404
from model import *

def get_vars(request):
    return_obj = {}

    if request.is_ajax() and request.method == 'POST':

        try:
            info = request.POST
            region = info.get("region")
            variables = get_variables(region)


            return_obj["variables"] = variables
            return_obj["success"] = "success"
            return_obj["region"]  = region

        except Exception as e:
            return_obj["error"] = e

        return JsonResponse(return_obj)

def get_dates(request):
    return_obj = {}

    if request.is_ajax() and request.method == 'POST':

        info = request.POST
        variable = info.get("variable")
        region = info.get("region")

        try:
            dates = get_times(region, variable)

            return_obj["variable"] = variable
            return_obj["region"] = region
            return_obj["dates"] = dates
            return_obj["success"] = "success"

        except Exception as e:
            return_obj["error"] = e

        return JsonResponse(return_obj)

def get_raster(request):
    return_obj = {}

    if request.is_ajax() and request.method == 'POST':
        try:
            info = request.POST
            variable = info.get("variable")
            region = info.get("region")
            date = info.get("date")

            storename, mean, stddev, min, max = get_selected_raster(region,variable,date)
            color_range = calc_color_range(min,max)

            return_obj["storename"] = storename
            return_obj["mean"] = mean
            return_obj["stddev"] = stddev
            return_obj["min"] = min
            return_obj["max"] = max
            return_obj["scale"] = color_range
            return_obj["variable"] = variable
            return_obj["region"] = region
            return_obj["date"] = date
            return_obj["success"] = "success"

        except Exception as e:
            return_obj["error"] = str(e)+ "From ajax"

        return JsonResponse(return_obj)

def get_vic_plot(request):
    return_obj = {}
    context = {}

    if request.is_ajax() and request.method == 'POST':
        info = request.POST

        variable = info.get("variable")
        region = info.get("region")
        return_obj["variable"] = variable
        return_obj["region"] = region

        point = request.POST['point']
        polygon = request.POST['polygon']

        if point:
            try:
                mean, stddev, min, max, time_series = get_vic_point(region,variable,point)
                return_obj["mean"] = mean
                return_obj["stddev"] = stddev
                return_obj["min"] = min
                return_obj["max"] = max
                return_obj["point"] = point
                return_obj["time_series"] = time_series
                return_obj["variable"] = variable
                return_obj["interaction"] = "point"
                return_obj["success"] = "success"
                return JsonResponse(return_obj)

            except Exception as e:
                return_obj["error"] = "Error Retrieving Data"
                return JsonResponse(return_obj)

        if polygon:
            try:
                mean, stddev, min, max, time_series = get_vic_polygon(region,variable,polygon)
                return_obj["mean"] = mean
                return_obj["stddev"] = stddev
                return_obj["min"] = min
                return_obj["max"] = max
                return_obj["point"] = point
                return_obj["time_series"] = time_series
                return_obj["variable"] = variable
                return_obj["interaction"] = "polygon"
                return_obj["success"] = "success"
                return JsonResponse(return_obj)

            except Exception as e:
                return_obj["error"] = "Error Retrieving Data"
                return JsonResponse(return_obj)





def get_ensemble(request):
    return_obj = {}

    if request.is_ajax() and request.method == 'POST':
        info = request.POST

        gid = info.get("gid")
        schema = info.get("schema")

        ensembles = get_dssat_ensemble(gid,schema)
        return_obj["gid"] = gid
        return_obj["schema"] = schema
        return_obj["ensembles"] = ensembles
        return_obj["success"] = "success"

        return JsonResponse(return_obj)

def get_ens_values(request):
    return_obj = {}

    if request.is_ajax() and request.method == 'POST':
        info = request.POST

        try:

            gid = info.get("gid")
            schema = info.get("schema")
            ensemble = info.get("ensemble")
            if "avg" in ensemble:
                wsgd_series,lai_series,gwad_series,low_gwad_series,high_gwad_series,ensemble_info = get_dssat_values(gid,schema,ensemble)
                return_obj["gid"] = gid
                return_obj["schema"] = schema
                return_obj["ensemble"] = ensemble
                return_obj["wsgd_series"] = wsgd_series
                return_obj["lai_series"] = lai_series
                return_obj["gwad_series"] = gwad_series
                return_obj["low_gwad_series"] = low_gwad_series
                return_obj["high_gwad_series"] = high_gwad_series
                return_obj["ensemble_info"] = ensemble_info
                return_obj["success"] = "success"

                return JsonResponse(return_obj)
            else:
                wsgd_series, lai_series, gwad_series = get_dssat_values(gid, schema, ensemble)
                return_obj["gid"] = gid
                return_obj["schema"] = schema
                return_obj["ensemble"] = ensemble
                return_obj["wsgd_series"] = wsgd_series
                return_obj["lai_series"] = lai_series
                return_obj["gwad_series"] = gwad_series
                return_obj["success"] = "success"
                return JsonResponse(return_obj)

        except Exception as e:

            return_obj["error"] = "error"
            return JsonResponse(return_obj)



def get_schema_yield(request):
    return_obj = {}

    if request.is_ajax() and request.method == 'POST':
        info = request.POST

        schema = info.get("schema")

        yield_data = calculate_yield(schema)

        return_obj["yield"] = yield_data
        return_obj["schema"] = schema
        return_obj["success"] = "success"

        return JsonResponse(return_obj)

