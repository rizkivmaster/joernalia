var IncomeRow = React.createClass({
	render: function(){
		return(
				<tr class='incomeRow'>
					<td>
						this.props.invoiceId
					</td>
					<td>
						this.props.from
					</td>
					<td>
						this.props.date
					</td>
					<td>
						this.props.total
					</td>
					<td>
						this.props.status
					</td>
				</tr>
			)
	}
});

var examples = [
	[]
]
var IncomeTable = React.createClass({
	render: function(){
		return(
			<table class='incomeTable'>
			<theader>
				<td>
					'Invoice ID'
				</td>
				<td>
					'From'
				</td>
				<td>
					'Date'
				</td>
				<td>
					'Total'
				</td>
				<td>
					'Status'
				</td>

			</theader>
			</table>
			)
	}
})