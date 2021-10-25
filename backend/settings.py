DEBUG = True
SCHEMA_ENDPOINT = '/schema'
EMBEDDING = True
DATE_FORMAT = '%Y-%m-%d'
if DEBUG:
    MONGO_URI = 'mongodb://admin:adminpassword@mongo:27017/mtdashboard_app'
else:
    MONGO_URI = 'mongodb+srv://mtdashboard:lWEArsTnq7VYwl5x@spb-cluster.1rggp.mongodb.net/mtdashboard_app?retryWrites=true&w=majority&ssl=true'
RENDERERS = [
    'eve.render.JSONRenderer', 
    # 'eve.render.XMLRenderer'
]

# DOMAINS SETUP
# Resources will be based on the departments
DOMAIN = {
    'targets': {
        'resource_methods': ['GET', 'POST'], 
        'schema': {
            'resource': {
                'type': 'string',
                'meta': {
                    'verbose_name': 'Resource',
                    'hint': 'Resource name.'
                }
            },
            'target_name': {
                'type': 'string',
                'meta': {
                    'verbose_name': 'Target Name',
                    'hint': 'Refernce key.'
                }
            },
            'target_value': {
                'type': 'string',
                'meta': {
                    'verbose_name': 'Target Value',
                    'hint': 'Target value.'
                }
            }
        }
    },
    'notifications': {
        'resource_methods': ['GET', 'POST'],
    },
    'utilities': {
        'resource_methods': ['GET', 'POST'],
        'schema': {
            'date': {
                'type': 'dict',
                'meta': {
                    'verbose_name': 'Date'
                },
                'schema': {
                    'date': {
                        'type': 'datetime',
                        'meta': {
                            'verbose_name': 'Date'
                        }
                    },
                    'week': {
                        'type': 'integer',
                        'allowed': [ i for i in range(54) ],
                        'meta': {
                            'verbose_name': 'Week',
                            'hint': 'ISO Week Number',
                        }
                    },
                }
            },
            'cost': {
                'type': 'dict',
                'schema': {
                    'water_consumption': {
                        'schema': {
                            'ro_plant': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'RO Plant'
                                }
                            },
                            'back_wash': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Back Wash'
                                }
                            },
                            'ro_concentrate_loss': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'RO Concentrate Loss in %'
                                }
                            },
                            'ro_bank_two_flow': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'RO Bank 2 Flow in %'
                                }
                            },
                            'cooling_tower_and_condensers': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'WM014 Cooling Tower & Condensers'
                                }
                            },
                            'boiler_feed': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Boiler Feed WM015'
                                }
                            },
                            'co2_gas_washer': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'CO2 Gas Washer'
                                }
                            }
                        }
                    },
                    'electricity_consumption': {
                        'schema': {
                            'santec_cooling_consumption': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'SCANTEC COOLING CONSUMPTION',
                                    'hint': ' (KWH/HLPR) (EM 113, 124, 131, 134, 144, 232)'
                                }
                            },
                            'atlas_copco_consumption': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'ATLAS COPCO CONSUMPTION',
                                    'hint': '(KWH/HLPR) (EM 133,211,212,324)'
                                }
                            },
                            'consumption_euwa': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'CONSUMPTION EUWA',
                                    'hint': '(KWH/HLPR) (EM 1112, 337)'
                                }
                            },
                            'haffmans_consumption': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'HAFFMANS CONSUMPTION',
                                    'hint': '(KWH/HLPR) (EM 241)'
                                }
                            }
                        }
                    },
                    'thermal_energy_consumption': {
                        'schema': {
                            'hkb_boiler_losses': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'HKB BOILER LOSSES (MJ/HLPR) '
                                }
                            },
                            'hkb_deaerator_thermal': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'HKB DEAERATOR THERMAL',
                                    'hint': '(MJ/HLPR) (SM 008)'
                                }
                            },
                            'wtp_thermal': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'WTP THERMAL',
                                    'hint': '(MJ/HLPR) (SM 007)'
                                }
                            }
                        } 
                    }
                }
            }
        }
    },
    'quality': {
        'resource_methods': ['GET', 'POST'],
        'schema': {
            'date': {
                'type': 'dict',
                'meta': {
                    'verbose_name': 'Date'
                },
                'schema': {
                    'start': {
                        'type': 'datetime',
                        'meta': {
                            'verbose_name': 'Date'
                        }
                    },
                    'week': {
                        'type': 'integer',
                        'allowed': [ i for i in range(54) ],
                        'meta': {
                            'verbose_name': 'Week',
                            'hint': 'ISO Week Number',
                        }
                    },
                }
            },
            'justified_market_complaints': {
                'type': 'integer',
                'meta': {
                    'verbose_name': 'Justified Market Complaints'
                }
            },
            'ftr_packaging': {
                'type': 'dict',
                'schema': {
                    'filling_levels': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Filling levels'
                        }
                    },
                    'foreign_gas_in_headspace': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Foreign gas in headspace'
                        }
                    },
                    'pcqi': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Packaging Consumer Quality Index (PCQI)'
                        }
                    },
                    'pasteurisation_units': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Pasteurisation Units'
                        }
                    },
                    'plqi': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Packaging Logistics Quality Index (PLQI)'
                        }
                    }
                },
            },
            'ftr_finished_product': {
                'type': 'dict',
                'schema': {
                    'original_extract': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Original extract'
                        }
                    },
                    'bitterness': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Bitterness'
                        }
                    },
                    'foam_stability': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Foam Stability'
                        }
                    },
                    'color': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Color'
                        }
                    },
                    'seven_day_turbidity': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': '7 Day Turbidity'
                        }
                    }
                }
            }, 
            'ftr_beer_production': {
                'type': 'dict',
                'schema': {
                    'ftr_brewhouse': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'FTR Brewhouse'
                        }
                    },
                    'ftr_fermentation': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'FTR Fermentation'
                        }
                    },
                    'ftr_bright_beer': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'FTR Bright Beer'
                        }
                    },
                }
            },
            'ftr_microbiology': {
                'type': 'dict',
                'schema': {
                    'ftr_micro_beer_production': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'FTR Micro Beer production'
                        }
                    },
                    'ftr_micro_packaging': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'FTR Micro Packaging'
                        }
                    }
                }
            }
        }
    },
    'packaging': {
        'resource_methods': ['GET', 'POST'],
        'item_methods': ['GET', 'DELETE', 'PATCH'],
        'schema': {
            'date': {
                'type': 'dict',
                'meta': {
                    'verbose_name': 'Date'
                },
                'schema': {
                    'start': {
                        'type': 'datetime',
                        'meta': {
                            'verbose_name': 'Week Start Date'
                        }
                    },
                    'week': {
                        'type': 'integer',
                        'allowed': [ i for i in range(54) ],
                        'meta': {
                            'verbose_name': 'Week',
                            'hint': 'ISO Week Number',
                        }
                    },
                }
            },
            'production': {
                'type': 'dict',
                'meta': {
                    'verbose_name': 'Production'
                },
                'schema': {
                    'plan': {
                        'type': 'dict',
                        'meta': {
                            'verbose_name': 'Plan'
                        },
                        'schema': {
                            'volume_packed_plan': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Volume Packed (Plan)'
                                }
                            },
                            'volume_packed_actual': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Volume Packed (Actual)'
                                }
                            },
                            'variance': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Variance'
                                }
                            },
                        }
                    }
                    #'conformance_to_schedule': {}
                }
            },
            'cost': {
                'type': 'dict',
                'meta': {
                    'verbose_name': 'Cost'
                },
                'schema': {
                    'water_consumption': {
                        'type': 'dict',
                        'meta': {
                            'verbose_name': 'Water Consumption'
                        },
                        'schema': {
                            'packaging_unmetered': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Packaging Unmetered'
                                }
                            },
                            'hose_rail_can_pasto': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Hose Rail Can Pasto'
                                }
                            },
                            'hose_rail_bottle_depal': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Hose Rail Bottle Depal'
                                }
                            },
                            'can_rinser': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Can Rinser (HL/Hlbo) WM029'
                                }
                            },
                            'bottle_conveyor': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Bottle Conveyor'
                                }
                            },
                            'bottle_pasteurizer': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Bottle Pasteurizer (HL/Hlbo) WM026'
                                }
                            },
                            'bottle_washer': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Bottle Washer (HL/Hlbo) WM027'
                                }
                            }
                        }
                    },
                    'electricity_consumption': {
                        'type': 'dict',
                        'meta': {
                            'verbose_name': 'Electricity Consumption'
                        },
                        'schema': {
                            'bottle_line_distribution_boards': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Bottle Line Distribution Boards'
                                }
                            },
                            'bottle_line_conveyors': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Bottle Line Conveyors (KWH/HLBO) (EM 132, 243, 326)'
                                }
                            },
                            'bottle_pasteuriser': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Bottle Pasteurizer (KWH/HLBO) (EM 221)'
                                }
                            },
                            'bottle_washer': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Bottle Washer (KWH/HLBO) (EM 244)'
                                }
                            },
                            'bottle_kister': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Bottle Kister'
                                }
                            },
                            'can_line_electricity_consumption': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Can Line Electricity Consumption (KWH/HLCA) (EM224)'
                                }
                            }
                        }
                    },
                    'opi_nona_can_line': {
                        'type': 'dict',
                        'meta': {
                            'verbose_name': 'OPI NONA Can Line'
                        },
                        'schema': {
                            'planned_stops': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Planned Stops'
                                }
                            },
                            'change_over': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Change Over'
                                }
                            },
                            'external_stops': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'External Stops'
                                }
                            },
                            'breakdown': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Breakdown'
                                }
                            },
                            'minor_stops_and_speed_loss': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Minor Stops & Speed loss'
                                }
                            },
                            'rejects_and_rework': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Rejects & Rework'
                                }
                            }
                        }
                    },
                    'opi_nona_bottle_line': {
                        'type': 'dict',
                        'meta': {
                            'verbose_name': 'OPI NONA Bottle Line'
                        },
                        'schema': {
                            'planned_stops': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Planned Stops'
                                }
                            },
                            'change_over': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Change Over'
                                }
                            },
                            'external_stops': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'External Stops'
                                }
                            },
                            'breakdown': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Breakdown'
                                }
                            },
                            'minor_stops_and_speed_loss': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Minor Stops & Speed loss'
                                }
                            },
                            'rejects_and_rework': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Rejects & Rework'
                                }
                            }
                        }
                    },
                }
            },
            'safety_tags': {
                'type': 'dict',
                'meta': {
                    'verbose_name': 'Safety Tags'
                }
            }
        },
        'owpm': {
            'type': 'decimal',
            'meta': {
                'verbose_name': 'One Week PackMat'
            }
        }
    },
    'brewing': {
        'resource_methods': ['GET', 'POST'],
        'schema': {
            'date': {
                'type': 'dict',
                'meta': {
                    'verbose_name': 'Date'
                },
                'schema': {
                    'start': {
                        'type': 'datetime',
                        'meta': {
                            'verbose_name': 'Week Start'
                        }
                    },
                    'week': {
                        'type': 'integer',
                        'allowed': [ i for i in range(54) ],
                        'meta': {
                            'verbose_name': 'Week',
                            'hint': 'ISO Week Number',
                        }
                    },
                }
            },
            'production': {
                'type': 'dict',
                'schema': {
                    'volume_brewed_plan': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Volume Brewed Plan (Cold Wort)'
                        }
                    },
                    'volume_brewed_actual': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Volume Brewed Actual (Cold Wort)'
                        }
                    },
                    'volume_brewed_variance': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Volume Brewed Variance'
                        }
                    },
                    'brewing_conformance_to_schedule': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Brewing Conformance to Schedule'
                        }
                    }
                }
            },
            'cost': {
                'type': 'dict',
                'schema': {
                    'water_consumption': {
                        'type': 'dict',
                        'schema': {
                            'total_water_consumption_brewhouse': {
                                'type': 'decimal',
                                'meta':{
                                    'verbose_name': 'Total Water Consumption Brewhouse (HL/HLCOLD WORT)'
                                }
                            },
                            'cellar_daw': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': '1 Cellar DAW (HL/HLCOLD WORT) WM 036'
                                }
                            }
                        }
                    },
                    'electricity_consumption': {
                        'type': 'dict',
                        'schema': {
                            'brewhouse': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Bewhouse (KWH/HLCO) (EM 213, 222, 234)'
                                }
                            },
                            'cellars_and_bmf': {
                                'type': 'decimal',
                                'meta': {
                                    'verbose_name': 'Cellars and BMF (KWH/HLCO) (EM 142, 312, 325) '
                                }
                            }
                        }
                    },
                    'thermal_consumption': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Thermal Consumption'
                        }
                    },
                    'extract_losses_actual': {
                        'type': 'decimal',
                        'meta': {
                            'verbose_name': 'Extract Losses (Actual)'
                        }
                    }
                }
            },
        }
    },
    'logistics': {
        'resource_methods': ['GET', 'POST'],
    },
    'safety': {
        'resource_methods': ['GET', 'POST'],
        'schema': {
            'swat' : {
                'type': 'dict',
                'schema': {
                    'number_of_accidents': {
                        'type': 'integer'
                    },
                    'planned_observations': {
                        'type': 'integer'
                    },
                    'actual_observations': {
                        'type': 'integer'
                    },
                    'conformance_to_schedule': {
                        'type': 'dict',
                        'schema': {
                            'packaging': {
                                'type': 'dict',
                                'schema': {
                                    'planned_observations': {
                                        'type': 'integer'
                                    },
                                    'actual_observations': {
                                        'type': 'integer'
                                    }
                                }
                            },
                            'brewing': {
                                'type': 'dict',
                                'schema': {
                                    'planned_observations': {
                                        'type': 'integer'
                                    },
                                    'actual_observations': {
                                        'type': 'integer'
                                    },
                                }
                            },
                            'logistics': {
                                'type': 'dict',
                                'schema': {
                                    'planned_observations': {
                                        'type': 'integer'
                                    },
                                    'actual_observations': {
                                        'type': 'integer'
                                    }
                                }
                            },
                            'utilities': {
                                'type': 'dict',
                                'schema': {
                                    'planned_observations': {
                                        'type': 'integer'
                                    },
                                    'actual_observations': {
                                        'type': 'integer'
                                    },
                                }
                            },
                            'quality': {
                                'type': 'dict',
                                'schema': {
                                    'planned_observations': {
                                        'type': 'integer'
                                    },
                                    'actual_observations': {
                                        'type': 'integer'
                                    }
                                }
                            },
                            'brewery_manager': {
                                'type': 'dict',
                                'schema': {
                                    'planned_observations': {
                                        'type': 'integer'
                                    },
                                    'actual_observations': {
                                        'type': 'integer'
                                    }
                                }
                            }
                        }
                    }
                }
            },
            'safety_tags': {
                'type': 'dict',
                'schema': {
                    'tags_raised': {
                        'type': 'integer',
                    },
                    'tags_closed': {
                        'type': 'integer'
                    },
                    'average_time_to_solve': {
                        'type': 'dict',
                        'schema': {
                            'packaging': {
                                'type': 'dict',
                                'schema': {
                                    'cards_raised': {
                                        'type': 'integer'
                                    },
                                    'cards_closed': {
                                        'type': 'integer'
                                    },
                                    'average_time_to_solve': {
                                        'type': 'integer'
                                    }
                                }
                            },
                            'brewing': {
                                'type': 'dict',
                                'schema': {
                                    'cards_raised': {
                                        'type': 'integer'
                                    },
                                    'cards_closed': {
                                        'type': 'integer'
                                    },
                                    'average_time_to_solve': {
                                        'type': 'integer'
                                    }
                                }
                            },
                            'logistics': {
                                'type': 'dict',
                                'schema': {
                                    'cards_raised': {
                                        'type': 'integer'
                                    },
                                    'cards_closed': {
                                        'type': 'integer'
                                    },
                                    'average_time_to_solve': {
                                        'type': 'integer'
                                    }
                                }
                            },
                            'utilities': {
                                'type': 'dict',
                                'schema': {
                                    'cards_raised': {
                                        'type': 'integer'
                                    },
                                    'cards_closed': {
                                        'type': 'integer'
                                    },
                                    'average_time_to_solve': {
                                        'type': 'integer'
                                    }
                                }
                            },
                            'quality': {
                                'type': 'dict',
                                'schema': {
                                    'cards_raised': {
                                        'type': 'integer'
                                    },
                                    'cards_closed': {
                                        'type': 'integer'
                                    },
                                    'average_time_to_solve': {
                                        'type': 'integer'
                                    }
                                }
                            },
                            'brewery_manager': {
                                'type': 'dict',
                                'schema': {
                                    'cards_raised': {
                                        'type': 'integer'
                                    },
                                    'cards_closed': {
                                        'type': 'integer'
                                    },
                                    'average_time_to_solve': {
                                        'type': 'integer'
                                    }
                                }
                            }
                        }
                    }
                }
            },
        }
    }
}