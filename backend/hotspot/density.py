from flask import Blueprint, jsonify

from src.utils import get_networkGraph
from src.visualisation import plot_hotspot

hotspot_bp = Blueprint('hotspot', __name__, url_prefix="/api/v1/hotspot")


@hotspot_bp.route('<session_id>/density')
def compute_density(session_id):
    """
    :Function: Compute the density of the network
    :param session_id: the session id
    :type session_id: str
    :return: the density of the network
    :rtype: json
    """
    G = get_networkGraph(session_id)

    df, filename = plot_hotspot(G)

    df_json = df.to_json(orient='split')

    return jsonify({"message": "Success", "data": df_json, "filename": filename})
