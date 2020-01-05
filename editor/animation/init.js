//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        function unrulyCanvas(dom, data) {

            if (! data || ! data.ext) {
                return
            }

            // hide right-answer
            $(dom.parentNode).find(".answer").remove()

            const input = data.in
            const output = data.out
            const addon = data.ext.result_addon
            const result = data.ext.result
            const [width, height] = [input[0].length, input.length]

            /*----------------------------------------------*
             *
             * attr
             *
             *----------------------------------------------*/
            const attr = {
                grid: {
                    'stroke-width': 0.5*(6/Math.min(14, width)) + 'px',
                    'stroke': '#dfe8f7',
                },
                background: {
                    'stroke-width': 0,
                    'fill': 'white',
                },
                cell: {
                    normal: {
                        W: {
                            'stroke-width': 0,
                            'fill': '#65A1Cf',
                        },
                        B: {
                            'stroke-width': 0,
                            'fill': '#294270',
                        },
                        '.': {
                            'stroke-width': 0,
                        },
                    },
                    error: {
                        W: {
                            'stroke-width': 0,
                            'fill': '#FABA00',
                        },
                        B: {
                            'stroke-width': 0,
                            'fill': '#F0801A',
                        },
                    }
                },
            }

            /*----------------------------------------------*
             *
             * paper
             *
             *----------------------------------------------*/
            const os = 10
            const cell_length = 320 / width
            const paper = Raphael(dom, 320, cell_length*height+os, 0, 0)

            // background (white)
            paper.rect(0, os, 320, cell_length*height).attr(attr.background)

            /*----------------------------------------------*
             *
             * draw cell
             *
             *----------------------------------------------*/
            const isvalid_output = Array.isArray(addon);
            (result || isvalid_output ? output : input).forEach((row, y)=>{
                row.split('').forEach((color, x)=>{
                    const cell = paper.rect(x*cell_length, y*cell_length+os, cell_length, cell_length)
                    cell.attr(attr.cell.normal[color])

                    // error indication
                    if (! result && isvalid_output) {
                        const [type, num] = addon.slice(1, 3)
                        if (type == 'row' && y == num || type == 'column' && x == num) {
                            cell.attr(attr.cell.error[color])
                        } else if (type == 'cell') {
                            for (let [cy, cx] of num) {
                                if (cy == y && cx == x) {
                                    cell.attr(attr.cell.error[color])
                                }
                            }
                        }
                    }
                })
            })

            /*----------------------------------------------*
             *
             * draw grid
             *
             *----------------------------------------------*/
            for (let y = 0; y < height; y += 1) {
                paper.rect(0, y*cell_length+os, 320, cell_length).attr(attr.grid)
            }
            for (let x = 0; x < width; x += 1) {
                paper.rect(x*cell_length, os, cell_length, cell_length*height).attr(attr.grid)
            }

            /*----------------------------------------------*
             *
             * message
             *
             *----------------------------------------------*/
            if (! result) {
                const message = Array.isArray(addon) ? addon[0] : addon
                $(dom).addClass('output').prepend(
                    '<div>' + message + '</div>').css(
                        {'border': '0','display': 'block',})
            }
        }

        var $tryit;

        var io = new extIO({
            multipleArguments: false,
            functions: {
                python: 'unruly',
                // js: 'unruly'
            },
            animation: function($expl, data){
                unrulyCanvas(
                    $expl[0],
                    data,
                );
            }
        });
        io.start();
    }
);
