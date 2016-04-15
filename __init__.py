# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MapFinds
                                 A QGIS plugin
 This plugin lets you create an layer of arch findings.
                             -------------------
        begin                : 2016-04-15
        copyright            : (C) 2016 by Marco Kultus
        email                : mk.archaeo@gmail.com
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
    """Load MapFinds class from file MapFinds.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .map_finds import MapFinds
    return MapFinds(iface)
