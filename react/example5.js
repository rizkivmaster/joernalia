var IncomeTable = React.createClass({displayName: "IncomeTable",
	render: function(){
		return(
			React.createElement("table", {class: "incomeTable"}, 
			React.createElement("theader", null, 
				React.createElement("td", null, 
					"Invoice ID"
				), 
				React.createElement("td", null, 
					"From"
				), 
				React.createElement("td", null, 
					"Date"
				), 
				React.createElement("td", null, 
					"Total"
				), 
				React.createElement("td", null, 
					"Status"
				)

			)
			)
			);
	}
});

ReactDOM.render(React.createElement(IncomeTable, null), document.getElementById('content'));