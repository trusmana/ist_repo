var chat_room_id = undefined;
var last_received = 0;

function init_chat(chat_id, html_el_id) {
	chat_room_id = chat_id;
	layout_and_bind(html_el_id);
	sync_messages();
}

var img_dir = "/static/img/";

function sync_messages() {
    $.ajax({
        type: 'POST',
        data: {id:window.chat_room_id},
        url:'/chat/sync/',
		dataType: 'json',
		success: function (json) {
        	last_received = json.last_message_id;
		}        
    });
	
	setTimeout("get_messages()", 2000);
}


function layout_and_bind(html_el_id) {
		// layout stuff
		var html = '<div id="chat-messages-container">'+
		'<div id="chat-messages"> </div>'+
		'<div id="chat-last"> </div>'+
		'</div>'+
		'<form id="chat-form">'+
		'<input name="message" type="text" class="message" />'+
		'<input type="submit" value="SEND!!!"/>'+
		'</form>';
		
		$("#"+html_el_id).append(html);
		
		// event stuff
    	$("#chat-form").submit( function () {
            var $inputs = $(this).children('input');
            var values = {};
            
            $inputs.each(function(i,el) { 
            	values[el.name] = $(el).val();
            });
			values['chat_room_id'] = window.chat_room_id;
        	
        	$.ajax({
                data: values,
                dataType: 'json',
                type: 'post',
                url: '/chat/send/'
            });
            $('#chat-form .message').val('');
            return false;
	});
};


function get_messages() {
    $.ajax({
        type: 'POST',
        data: {id:window.chat_room_id, offset: window.last_received},
        url:'/chat/receive/',
		dataType: 'json',
		success: function (json) {
			var scroll = false;
		
			// first check if we are at the bottom of the div, if we are, we shall scroll once the content is added
			var $containter = $("#chat-messages-container");
			if ($containter.scrollTop() == $containter.attr("scrollHeight") - $containter.height())
				scroll = true;

			// add messages
			$.each(json, function(i,m){
				if (m.type == 's')
					$('#chat-messages').append('<div class="system">' + replace_emoticons(m.message) + '</div>');
				else if (m.type == 'm') 	
					$('#chat-messages').append('<div class="message"><div class="author">'+m.author+'</div>'+replace_emoticons(m.message) + '</div>');
				else if (m.type == 'j') 	
					$('#chat-messages').append('<div class="join">'+m.author+' Online</div>');
				else if (m.type == 'l') 	
					$('#chat-messages').append('<div class="leave">'+m.author+' Offline</div>');
					
				last_received = m.id;
			})
			
			// scroll to bottom
			if (scroll)
				$("#chat-messages-container").animate({ scrollTop: $("#chat-messages-container").attr("scrollHeight") }, 500);
		}        
    });
    
    // wait for next
    setTimeout("get_messages()", 2000);
}

/**
 * Tells the chat app that we are joining
 */
function chat_join() {
	$.ajax({
		async: false,
        type: 'POST',
        data: {chat_room_id:window.chat_room_id},
        url:'/chat/join/',
    });
}

/**
 * Tells the chat app that we are leaving
 */
function chat_leave() {
	$.ajax({
		async: false,
        type: 'POST',
        data: {chat_room_id:window.chat_room_id},
        url:'/chat/leave/',
    });
}

// attach join and leave events
$(window).load(function(){chat_join()});
$(window).unload(function(){chat_leave()});

// emoticons
var emoticons = {                 
	'>:d' : 'emoticon_evilgrin.png',
    'sip' :'sip.png',
    'ok':'sip.png',
	':d' : 'emoticon_grin.png',
	'=d' : 'emoticon_happy.png',
	':\\)' : 'emoticon_smile.png',
	':o' : 'emoticon_surprised.png',
	':p' : 'emoticon_tongue.png',
	':\\(' : 'emoticon_unhappy.png',
	':3' : 'emoticon_waii.png',
	';\\)' : 'emoticon_wink.png',
	'\\(ball\\)' : 'sport_soccer.png'
}

function replace_emoticons(text) {
	$.each(emoticons, function(char, img) {
		re = new RegExp(char,'g');
		// replace the following at will
		text = text.replace(re, '<img src="'+img_dir+img+'" />');
	});
	return text;
}

