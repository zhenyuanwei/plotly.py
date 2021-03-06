import _plotly_utils.basevalidators


class RangemodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='rangemode', parent_name='layout.yaxis', **kwargs
    ):
        super(RangemodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='style',
            values=['normal', 'tozero', 'nonnegative'],
            **kwargs
        )
