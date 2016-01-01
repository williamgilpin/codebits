// searches all textframes in document for term (like the special character \' or the phrase blah) and replaces with the phrase replace_string

var active_doc = app.activeDocument;  
  
var search_string = /\'/gi; // g for global search, remove i to make a case sensitive search  
var replace_string = "";  
  
var text_frames = active_doc.textFrames;  
  
if (text_frames.length > 0)  
{  
    for (var i = 0 ; i < text_frames.length; i++)  
      {  
          var this_text_frame = text_frames[i];  
           var new_string = this_text_frame.contents.replace(search_string, replace_string);  
             
           if (new_string != this_text_frame.contents)  
               {  
                    this_text_frame.contents = new_string;  
               }  
      }  
}  
