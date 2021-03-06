# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Polygon_Maker
                                 A QGIS plugin
 Creates polygons in a grid formate
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-06-12
        copyright            : (C) 2018 by Jacob Blankeship
        email                : JBlankenship@wilburellis.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Polygon_Maker class from file Polygon_Maker.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Polygon_Maker import Polygon_Maker
    return Polygon_Maker(iface)
