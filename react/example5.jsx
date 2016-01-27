var IncomeTable = React.createClass({
	render: function(){
		return(
			<table class='incomeTable'>
			<theader>
				<td>
					Invoice ID
				</td>
				<td>
					From
				</td>
				<td>
					Date
				</td>
				<td>
					Total
				</td>
				<td>
					Status
				</td>

			</theader>
			</table>
			);
	}
});

ReactDOM.render(<IncomeTable/>, document.getElementById('content'));