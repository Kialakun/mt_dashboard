DEBUG = True
SCHEMA_ENDPOINT = '/schema'
DATE_FORMAT = '%Y-%m-%d'
EMBEDDING = True
MONGO_URI = 'mongodb+srv://ptdams:Dr9txHwBsGdKk8r@works-ptd-cluster.ztapj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true'
RENDERERS = [
    'eve.render.JSONRenderer', 
    # 'eve.render.XMLRenderer'
]

# DOMAINS SETUP
# Resources will be based on the departments
DOMAIN = {
    'notifications': {
        'resource_methods': ['GET', 'POST'],
    },
    'utilities': {
        'schema': {
            'date': {
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
                                'verbose_name': 'SCANTEC COOLING CONSUMPTION (KWH/HLPR) (EM 113, 124, 131, 134, 144, 232)'
                            }
                        },
                        'atlas_copco_consumption': {
                            'type': 'decimal',
                            'meta': {
                                'verbose_name': 'ATLAS COPCO CONSUMPTION (KWH/HLPR) (EM 133,211,212,324)'
                            }
                        },
                        'consumption_euwa': {
                            'type': 'decimal',
                            'meta': {
                                'verbose_name': 'CONSUMPTION EUWA (KWH/HLPR) (EM 1112, 337)'
                            }
                        },
                        'haffmans_consumption': {
                            'type': 'decimal',
                            'meta': {
                                'verbose_name': 'HAFFMANS CONSUMPTION (KWH/HLPR) (EM 241)'
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
                                'verbose_name': 'HKB DEAERATOR THERMAL (MJ/HLPR) (SM 008)'
                            }
                        },
                        'wtp_thermal': {
                            'type': 'decimal',
                            'meta': {
                                'verbose_name': 'WTP THERMAL (MJ/HLPR) (SM 007)'
                            }
                        }
                    } 
                }
            }
        }
    },
    'quality': {
        'schema': {
            'date': {
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
            'justified_market_complaints': {
                'type': 'integer',
                'meta': {
                    'verbose_name': 'Justified Market Complaints'
                }
            },
            'ftr_packaging': {
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
    },
    'packaging': {
        'resource_methods': ['GET', 'POST'],
        'schema': {
            'date': {
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
                'meta': {
                    'verbose_name': 'Production'
                },
                'schema': {
                    'plan': {
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
                'meta': {
                    'verbose_name': 'Cost'
                },
                'schema': {
                    'water_consumption': {
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
            'production': {
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
                'schema': {
                    'water_consumption': {
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
                    'schema': {
                        'packaging': {
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

            },
            'safety_tags': {
                'schema': {
                    'tags_raised': {
                        'type': 'integer',
                    },
                    'tags_closed': {
                        'type': 'integer'
                    },
                    'average_time_to_solve': {
                        'schema': {
                            'packaging': {
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