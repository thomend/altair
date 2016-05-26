# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T

from .. import _generated as schema


class Field(schema.FieldDef):
    """Wrapper for Vega-Lite FieldDef definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate: AggregateOp
        
    bin: Union(Bool, BinProperties)
        
    displayName: Unicode
        
    field: Unicode
        
    timeUnit: TimeUnit
        
    type: Union(Type, Unicode)
        
    value: Union(CFloat, Unicode, Bool)
        
    """
    # Traitlets
    shorthand = T.Unicode('')
    type = T.Union([schema.Type(), T.Unicode()],
                   allow_none=True, default_value=None)

    @T.observe('shorthand')
    def _shorthand_changed(self, change):
        D = parse_shorthand(change['new'])
        for key, val in D.items():
            setattr(self, key, val)

    @T.observe('type')
    def _type_changed(self, change):
        new = change['new']
        if new in TYPE_ABBR:
            self.type = INV_TYPECODE_MAP[new]

    # Class Attributes
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=None, bin=None, displayName=None, field=None, timeUnit=None, type=None, value=None, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, displayName=displayName, field=field, timeUnit=timeUnit, type=type, value=value)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(Field, self).__init__(**kwargs)

    def _infer_type(self, data):
        if isinstance(data, pd.DataFrame):
            if not self.type and self.field in data:
                self.type = infer_vegalite_type(data[self.field])
        if data is None:
            self.type = ''