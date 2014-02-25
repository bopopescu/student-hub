;(function(){

			// Menu settings
			$('#menuToggle, .menu2-close').on('click', function(){
				$('#menuToggle').toggleClass('active');
				$('body').toggleClass('body-push-toleft');
				$('#theMenu').toggleClass('menu2-open');
			});


})(jQuery)