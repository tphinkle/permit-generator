console.log("firewatch.js");


$( document ).ready(function() { //wait until body loads


		//Inputs that determine what fields to show
		var field_0 = $('#permit input:radio[name=field_0]');

		//Wrappers for all fields
    var field_0_0_form = $('#field_0_0_form');
		var field_0_1_form = $('#field_0_1_form');
		var field_0_2_form = $('#field_0_2_form');


		field_0.change(function(){ //when the rating changes
			var value=this.value;

			field_0_0_form.addClass('hidden'); //hide everything and reveal as needed
			if (value == 'Yes'){
				field_0_0_form.removeClass('hidden'); //show feedback_bad
			}

			field_0_1_form.addClass('hidden');
			if (value == 'Yes'){
				field_0_1_form.removeClass('hidden');
			}

			field_0_2_form.addClass('hidden');
			if (value == 'Yes'){
				field_0_2_form.removeClass('hidden');
			}

		});


		var field_0_1 = $('#permit input:radio[name=field_0_1]');

		var field_0_1_0_form = $('#field_0_1_0_form');
		var field_0_1_1_form = $('#field_0_1_1_form');

		field_0_1.change(function(){
			var value = this.value;


			field_0_1_0_form.addClass('hidden');

			if(value == 'Yes'){
				field_0_1_0_form.removeClass('hidden');
			}

			field_0_1_1_form.addClass('hidden');

			if(value == 'Yes'){
				field_0_1_1_form.removeClass('hidden');
			}

		})



});
