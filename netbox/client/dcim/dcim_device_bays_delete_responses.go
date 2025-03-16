// Code generated by go-swagger; DO NOT EDIT.

// Copyright 2018 The go-netbox Authors.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package dcim

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"

	"github.com/go-openapi/runtime"

	strfmt "github.com/go-openapi/strfmt"
)

// DcimDeviceBaysDeleteReader is a Reader for the DcimDeviceBaysDelete structure.
type DcimDeviceBaysDeleteReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *DcimDeviceBaysDeleteReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {

	case 204:
		result := NewDcimDeviceBaysDeleteNoContent()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil

	default:
		return nil, runtime.NewAPIError("unknown error", response, response.Code())
	}
}

// NewDcimDeviceBaysDeleteNoContent creates a DcimDeviceBaysDeleteNoContent with default headers values
func NewDcimDeviceBaysDeleteNoContent() *DcimDeviceBaysDeleteNoContent {
	return &DcimDeviceBaysDeleteNoContent{}
}

/*DcimDeviceBaysDeleteNoContent handles this case with default header values.

DcimDeviceBaysDeleteNoContent dcim device bays delete no content
*/
type DcimDeviceBaysDeleteNoContent struct {
}

func (o *DcimDeviceBaysDeleteNoContent) Error() string {
	return fmt.Sprintf("[DELETE /dcim/device-bays/{id}/][%d] dcimDeviceBaysDeleteNoContent ", 204)
}

func (o *DcimDeviceBaysDeleteNoContent) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
