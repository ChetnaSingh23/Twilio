
function count_rabbits() {

    for(var i=1; i<=3; i++) {


			<div id="comments">
			 {{#each comments}}
			 <h2><a href="/posts/{{../permalink}}#{{id}}">{{title}}</a></h2>
			 <div>{{body}}</div>
			 {{/each}}
			</div>
             }
}